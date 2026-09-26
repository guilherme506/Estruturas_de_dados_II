# Conway's Game of Life — Versão Otimizada

Uma implementação do **Conway's Game of Life** desenvolvida em Python, com foco na melhoria de desempenho em relação a uma implementação tradicional baseada em uma matriz que percorre todas as células do universo.

O projeto utiliza uma **estrutura de dados esparsa baseada em `set`**, testes automatizados e benchmarks para medir o impacto das otimizações realizadas.

---

## Sobre o projeto

O Conway's Game of Life é um autômato celular criado pelo matemático britânico **John Horton Conway**.

O jogo é executado em um universo bidimensional formado por células que podem estar em dois estados:

- **Viva**
- **Morta**

Cada célula possui oito vizinhos possíveis:

```text
┌───┬───┬───┐
│   │   │   │
├───┼───┼───┤
│   │ X │   │
├───┼───┼───┤
│   │   │   │
└───┴───┴───┘

X = célula atual

No jogo original a implementação tradicional pode representar o universo como uma matriz, para calcular uma nova geração, o programa precisa percorrer toda a matriz.
Entretanto isso gera um problema quando o universo é muito grande e possui poucas células vivas. Por exemplo:
    Se apenas 500 células estiverem vivas, uma implementação baseada em matriz ainda precisaria considerar uma quantidade enorme de posições vazias.

Na versão reproduzida, as células vivas são armazenadas em um  set[tuple[int, int]]
Fazendo com que somente as células vivas são armazenadas, permitindo trabalhar com um universo conceitualmente muito maior sem precisar criar uma matriz inteira.


