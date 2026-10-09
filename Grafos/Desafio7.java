import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Desafio7{

    public static void main(String[] args) {
        int[] pedida = {1, 1, 2, 3, 3, 4, 4, 6};
        String[] v = {"A", "B", "C", "D", "E", "F", "G", "H"};
        int n = v.length;

        titulo("DESAFIO 7 - SEQUENCIA DE GRAUS");
        System.out.println("Sequencia pedida (nao decrescente): " + formatar(pedida));

        // A recebe o maior grau, B o seguinte, ..., H o menor
        int[] alvo = new int[n];
        for (int i = 0; i < n; i++) {
            alvo[i] = pedida[n - 1 - i];
        }
        System.out.print("Grau desejado de cada vertice: ");
        for (int i = 0; i < n; i++) {
            System.out.print(v[i] + "=" + alvo[i] + (i < n - 1 ? ", " : "\n"));
        }

        // testes rapidos antes de construir
        int soma = 0;
        for (int d : pedida) {
            soma += d;
        }
        System.out.println("Soma dos graus pedidos = " + soma
                + (soma % 2 == 0 ? " (par -> " + soma / 2 + " arestas)" : " (impar -> impossivel)"));
        System.out.println("Maior grau = " + pedida[n - 1] + " <= n - 1 = " + (n - 1) + "? "
                + simNao(pedida[n - 1] <= n - 1));
        if (soma % 2 != 0 || pedida[n - 1] > n - 1) {
            System.out.println("Sequencia nao pode ser de grafo simples.");
            return;
        }

        // ---------------- construcao ----------------
        titulo("Construcao passo a passo (comecando pelo maior grau)");
        boolean[][] adj = new boolean[n][n];
        List<String> arestas = new ArrayList<String>();
        int[] resto = alvo.clone();
        int passo = 1;

        while (true) {
            int u = maiorResto(resto);
            if (resto[u] == 0) {
                break; // todos ja atingiram o grau desejado
            }
            int d = resto[u];
            Integer[] candidatos = ordenarPorResto(resto, u);

            StringBuilder sb = new StringBuilder();
            sb.append("Passo ").append(passo).append(": ").append(v[u])
              .append(" precisa de ").append(d).append(" aresta(s) -> liga com ");
            for (int t = 0; t < d; t++) {
                int w = candidatos[t];
                if (resto[w] == 0 || adj[u][w]) {
                    System.out.println("Nao foi possivel completar: a sequencia nao e grafica.");
                    return;
                }
                adj[u][w] = true;
                adj[w][u] = true;
                resto[w]--;
                arestas.add("(" + v[u] + "," + v[w] + ")");
                sb.append(v[w]).append(t < d - 1 ? ", " : "");
            }
            resto[u] = 0;
            System.out.println(sb);
            System.out.print("         graus que ainda faltam: ");
            for (int i = 0; i < n; i++) {
                System.out.print(v[i] + "=" + resto[i] + (i < n - 1 ? " " : "\n"));
            }
            passo++;
        }

        // ---------------- registro ----------------
        titulo("Conjunto de arestas E");
        System.out.println("E = {" + String.join(", ", arestas) + "}");

        titulo("Grau obtido de cada vertice");
        int[] obtido = new int[n];
        for (int i = 0; i < n; i++) {
            StringBuilder viz = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (adj[i][j]) {
                    obtido[i]++;
                    viz.append(v[j]).append(" ");
                }
            }
            System.out.println("  " + v[i] + " | grau " + obtido[i] + " | vizinhos: " + viz.toString().trim());
        }

        // ---------------- verificacao ----------------
        titulo("Verificacao");
        int[] ordenada = obtido.clone();
        Arrays.sort(ordenada);
        System.out.println("Sequencia obtida: " + formatar(ordenada));
        System.out.println("Igual a pedida?   " + simNao(Arrays.equals(ordenada, pedida)));

        int somaObtida = 0;
        for (int d : obtido) {
            somaObtida += d;
        }
        int m = arestas.size();
        System.out.println("Soma dos graus = " + somaObtida);
        System.out.println("Numero de arestas = " + m);
        System.out.println("Soma dos graus = 2 x numero de arestas? " + somaObtida + " = 2 x " + m
                + " = " + (2 * m) + " -> " + simNao(somaObtida == 2 * m));

        boolean temLaco = false;
        for (int i = 0; i < n; i++) {
            temLaco = temLaco || adj[i][i];
        }
        // como a matriz e booleana, um mesmo par nao pode ter duas arestas
        System.out.println("Grafo simples (sem lacos e sem arestas paralelas)? " + simNao(!temLaco));
    }

    // indice do vertice com maior resto (em empate, o de menor indice)
    static int maiorResto(int[] resto) {
        int u = 0;
        for (int i = 1; i < resto.length; i++) {
            if (resto[i] > resto[u]) {
                u = i;
            }
        }
        return u;
    }

    // demais vertices ordenados por resto decrescente (sort estavel: empate mantem ordem alfabetica)
    static Integer[] ordenarPorResto(final int[] resto, int excluir) {
        Integer[] idx = new Integer[resto.length - 1];
        int k = 0;
        for (int i = 0; i < resto.length; i++) {
            if (i != excluir) {
                idx[k++] = i;
            }
        }
        Arrays.sort(idx, (x, y) -> resto[y] - resto[x]);
        return idx;
    }

    static String formatar(int[] s) {
        StringBuilder sb = new StringBuilder("(");
        for (int i = 0; i < s.length; i++) {
            sb.append(s[i]).append(i < s.length - 1 ? ", " : "");
        }
        return sb.append(")").toString();
    }

    static String simNao(boolean b) {
        return b ? "sim" : "nao";
    }

    static void titulo(String t) {
        System.out.println();
        System.out.println("=== " + t + " ===");
    }
}
