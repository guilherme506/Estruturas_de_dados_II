# Conway's Game of Life — Design de Jogos sobre Árvores Avançadas

Projeto desenvolvido para a atividade prática de **Design de Jogos Educativos sobre Árvores Avançadas**, da disciplina de **Estruturas de Dados II**.

A atividade propõe utilizar um jogo ou modelo existente, analisar suas limitações e aplicar conceitos de estruturas de dados para criar um upgrade com finalidade educacional. O modelo escolhido foi o **Conway's Game of Life**, um autômato celular que simula a evolução de células em uma grade.

> **Integrantes:** Guilherme Galvão e Henrique Kirch  
> **Disciplina:** Estruturas de Dados II — Ciência da Computação

## 1. Modelo reutilizado

O Conway's Game of Life foi criado pelo matemático britânico **John Horton Conway**. O jogo utiliza uma grade bidimensional composta por células vivas e mortas.

Cada célula possui até oito vizinhos. A cada geração, as regras são aplicadas simultaneamente:

- uma célula viva sobrevive quando possui dois ou três vizinhos vivos;
- uma célula morta nasce quando possui exatamente três vizinhos vivos;
- uma célula viva morre por isolamento, superpopulação ou quando não atende às regras de sobrevivência.

O usuário pode criar células na grade e acompanhar a evolução da simulação geração após geração.

## 2. Relação com a atividade de Design de Jogos

O objetivo do designer de jogos é transformar conceitos teóricos de Estruturas de Dados II em uma experiência prática e visual. Neste projeto, o Conway's Game of Life foi usado como modelo-base para estudar o impacto da escolha da estrutura de dados na execução do jogo.

A proposta do upgrade foi melhorar o desempenho da implementação ingênua, que poderia representar todo o universo como uma matriz e percorrer inclusive as posições vazias.

Assim, a atividade relaciona:

- **modelo de jogo:** Conway's Game of Life;
- **problema técnico:** processamento desnecessário de uma grande quantidade de posições vazias;
- **upgrade:** representação esparsa das células vivas;
- **objetivo didático:** visualizar como a estrutura de dados influencia o desempenho do algoritmo.

Embora o tema da atividade esteja relacionado a árvores avançadas, a versão atual do projeto concentra a melhoria na representação esparsa usando `set`. Essa implementação serve como base para uma evolução futura que poderá utilizar uma árvore espacial, AVL, Rubro-Negra ou Árvore B para organizar as regiões e células do universo.

## 3. Limitação identificada

Uma implementação tradicional baseada em matriz precisa percorrer toda a grade para descobrir quais células devem nascer, sobreviver ou morrer. Esse comportamento se torna ineficiente quando:

- a grade é muito grande;
- poucas células estão vivas;
- a maior parte do espaço permanece vazia.

Por exemplo, mesmo que existam apenas algumas centenas de células vivas, uma matriz extensa ainda exigiria a análise de milhares ou milhões de posições vazias.

## 4. Solução implementada

Neste projeto, as células vivas são armazenadas como coordenadas em um conjunto:

```python
set[tuple[int, int]]
```

Cada célula é representada por uma tupla `(x, y)`. Dessa forma, somente as células vivas são armazenadas, evitando a criação de uma matriz completa.

Para calcular a próxima geração, o programa:

1. percorre as células vivas;
2. identifica os oito vizinhos de cada célula;
3. contabiliza quantas vezes cada posição aparece como vizinha;
4. aplica as regras do Conway's Game of Life;
5. cria um novo conjunto contendo as células vivas da próxima geração.

Essa estratégia é adequada para universos esparsos, pois o custo do processamento depende principalmente das células vivas e de seus vizinhos candidatos.

## 5. Implementação da atividade

O arquivo `src/conway/game.py` contém duas versões do cálculo da geração:

- `next_generation`: utiliza `collections.Counter` para contar os vizinhos;
- `next_generation_optimized`: utiliza um dicionário e uma compreensão de conjunto para realizar a mesma operação com menos abstrações intermediárias.

A função otimizada é utilizada pela interface gráfica.

A estrutura central do algoritmo é baseada nos oito deslocamentos possíveis:

```text
(-1, -1)  (0, -1)  (1, -1)
(-1,  0)           (1,  0)
(-1,  1)  (0,  1)  (1,  1)
```

## 6. Core loop do jogo

O core loop representa as ações que se repetem durante a experiência:

1. o usuário cria ou remove células na grade;
2. inicia a simulação ou avança manualmente uma geração;
3. o algoritmo calcula o próximo estado do universo;
4. a interface atualiza a grade, a geração e a quantidade de células vivas;
5. o usuário observa o comportamento e pode modificar o cenário.

A interface também possui um botão **Glider**, que insere um padrão conhecido do Conway's Game of Life para facilitar os testes.

## 7. Condições do jogo

- **Condição de vitória:** não existe. O objetivo é estudar e observar a evolução do autômato celular.
- **Condição de derrota:** não existe. A simulação pode estabilizar, repetir padrões ou ficar sem células vivas, mas não há encerramento por derrota.
- **Feedback da aplicação:** a interface mostra a geração atual e o número de células vivas.

A ausência de vitória e derrota é intencional, pois o foco da atividade é educacional e está relacionado à observação do comportamento do algoritmo e ao estudo de desempenho.

## 8. Interface da aplicação

A aplicação gráfica foi desenvolvida com **Tkinter** e oferece:

- grade interativa para criar e remover células;
- botão **Iniciar/Pausar**;
- botão **Próxima geração**;
- botão **Limpar**;
- botão **Glider**;
- indicador de geração e quantidade de células vivas.

A grade possui 60 colunas por 40 linhas, com células de 15 pixels.

## 9. Organização do projeto

```text
conway-life/
├── src/
│   └── conway/
│       ├── __init__.py
│       ├── app.py       # Interface gráfica
│       └── game.py      # Regras e cálculo das gerações
├── tests/               # Testes automatizados
├── pyproject.toml       # Configuração do projeto Python
├── uv.lock              # Dependências fixadas
└── README.md            # Documentação da atividade
```

## 10. Requisitos

- Python **3.14 ou superior**;
- Tkinter;
- `uv` para gerenciamento do ambiente, conforme a configuração do projeto;
- Pytest para executar os testes.

O projeto não possui dependências de execução externas. O `pyproject.toml` define o Pytest como dependência de desenvolvimento.

## 11. Como executar

A partir da pasta `conway-life`, sincronize o ambiente e execute a aplicação:

```bash
uv sync
uv run python -m conway.app
```

Para executar os testes:

```bash
uv run pytest
```

## 12. Complexidade e estrutura utilizada

A implementação armazena apenas as células vivas em um `set` de coordenadas. Em média:

- inserção de uma célula: `O(1)`;
- remoção de uma célula: `O(1)`;
- consulta de uma célula: `O(1)`;
- cálculo da geração: proporcional às células vivas e aos seus vizinhos candidatos.

Essa abordagem evita o custo de percorrer uma matriz inteira. O ganho é especialmente relevante quando o universo é grande e possui poucas células vivas.

## 13. Evolução para árvores avançadas

O projeto atual representa uma etapa do designer de jogos: a engenharia reversa do modelo e a melhoria de sua implementação.

Como próxima etapa, a mecânica pode ser ampliada para utilizar uma árvore avançada, por exemplo:

- **AVL:** manter regiões ou posições balanceadas para consultas eficientes;
- **Árvore Rubro-Negra:** organizar dinamicamente células e coordenadas mantendo balanceamento;
- **Árvore B:** armazenar grandes quantidades de posições em blocos e facilitar o acesso a universos extensos;
- **árvore espacial:** dividir o universo em regiões para consultar apenas áreas relevantes.

Nesse possível upgrade, o desempenho e as propriedades da árvore poderiam ser transformados em elementos visuais do jogo, como divisão de regiões, balanceamento, profundidade e custo das operações.

## 14. Conclusão da atividade

O projeto demonstra como a engenharia reversa de um jogo pode ser utilizada para estudar Estruturas de Dados II. A partir de um modelo conhecido, foi identificada uma limitação de desempenho e implementada uma representação mais adequada para cenários esparsos.

O Conway's Game of Life funciona, portanto, como um laboratório visual para comparar estratégias de armazenamento e processamento. A versão atual estabelece a base para que, em uma evolução posterior, árvores avançadas sejam incorporadas diretamente à mecânica do jogo.
