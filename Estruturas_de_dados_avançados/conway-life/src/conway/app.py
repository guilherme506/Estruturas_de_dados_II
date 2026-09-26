import tkinter as tk

from conway.game import next_generation_optimized


CELL_SIZE = 15
GRID_WIDTH = 60
GRID_HEIGHT = 40

BACKGROUND = "#111111"
GRID_COLOR = "#222222"
CELL_COLOR = "#00ff66"


class GameOfLife:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Conway's Game of Life")

        self.alive: set[tuple[int, int]] = set()
        self.running = False
        self.generation = 0

        self.canvas = tk.Canvas(
            root,
            width=GRID_WIDTH * CELL_SIZE,
            height=GRID_HEIGHT * CELL_SIZE,
            background=BACKGROUND,
            highlightthickness=0,
        )

        self.canvas.pack()

        controls = tk.Frame(root)
        controls.pack(pady=5)

        self.start_button = tk.Button(
            controls,
            text="Iniciar",
            command=self.toggle,
        )
        self.start_button.pack(side=tk.LEFT, padx=5)

        tk.Button(
            controls,
            text="Próxima geração",
            command=self.step,
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            controls,
            text="Limpar",
            command=self.clear,
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            controls,
            text="Glider",
            command=self.add_glider,
        ).pack(side=tk.LEFT, padx=5)

        self.info = tk.Label(
            root,
            text="Geração: 0 | Células: 0",
        )
        self.info.pack()

        self.canvas.bind("<Button-1>", self.toggle_cell)

        self.draw()

    def toggle_cell(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE

        cell = (x, y)

        if cell in self.alive:
            self.alive.remove(cell)
        else:
            self.alive.add(cell)

        self.draw()

    def step(self):
        self.alive = next_generation_optimized(self.alive)

        self.generation += 1

        self.draw()

    def toggle(self):
        self.running = not self.running

        if self.running:
            self.start_button.config(text="Pausar")
            self.run()
        else:
            self.start_button.config(text="Iniciar")

    def run(self):
        if not self.running:
            return

        self.step()

        self.root.after(50, self.run)

    def clear(self):
        self.running = False
        self.start_button.config(text="Iniciar")

        self.alive.clear()
        self.generation = 0

        self.draw()

    def add_glider(self):
        pattern = {
            (1, 0),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        }

        for x, y in pattern:
            self.alive.add((x + 5, y + 5))

        self.draw()

    def draw(self):
        self.canvas.delete("all")

        # Grade
        for x in range(GRID_WIDTH + 1):
            px = x * CELL_SIZE

            self.canvas.create_line(
                px,
                0,
                px,
                GRID_HEIGHT * CELL_SIZE,
                fill=GRID_COLOR,
            )

        for y in range(GRID_HEIGHT + 1):
            py = y * CELL_SIZE

            self.canvas.create_line(
                0,
                py,
                GRID_WIDTH * CELL_SIZE,
                py,
                fill=GRID_COLOR,
            )

        # Células vivas
        for x, y in self.alive:
            self.canvas.create_rectangle(
                x * CELL_SIZE + 1,
                y * CELL_SIZE + 1,
                (x + 1) * CELL_SIZE - 1,
                (y + 1) * CELL_SIZE - 1,
                fill=CELL_COLOR,
                outline="",
            )

        self.info.config(
            text=(
                f"Geração: {self.generation} | "
                f"Células: {len(self.alive)}"
            )
        )


def main():
    root = tk.Tk()

    GameOfLife(root)

    root.mainloop()


if __name__ == "__main__":
    main()
