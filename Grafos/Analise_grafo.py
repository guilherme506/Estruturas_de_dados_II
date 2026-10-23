rede = {
    "Ana": ["Bruno", "Carla", "Guilherme"],
    "Bruno": ["Ana", "Carla", "Diego", "Guilherme"],
    "Carla": ["Ana", "Bruno", "Elisa", "Guilherme"],
    "Diego": ["Bruno", "Elisa", "Felipe", "Guilherme"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"],
    "Guilherme": ["Ana", "Bruno", "Carla", "Diego"]
}

# Quantidade de usuarios
n = len(rede)

# Calculo do grau de cada usuario
for usuario, amigos in rede.items():
    print(usuario, "tem grau", len(amigos))

# Soma dos graus
soma_graus = sum(len(amigos) for amigos in rede.values())

# Cada amizade e contada duas vezes
arestas = soma_graus // 2

print("Total de usuarios:", n)
print("Soma dos graus:", soma_graus)
print("Total de amizades:", arestas)

# Calculo da densidade
densidade = (2 * arestas) / (n * (n - 1))

print(f"Densidade: {densidade:.2%}")
