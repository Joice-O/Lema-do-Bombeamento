#...
#Função que verifica se a cadeia está na linguagem L = { aⁿbⁿ|n≥0 }
def linguagem_a_n_b_n(w):
    n = len(w)
    meio = 0
    # Conta o número de 'a's e 'b's
    count_a = 0
    for c in w:
        if c == 'a':
            count_a += 1
        else:
            break
    count_b = n - count_a
    return w == 'a' * count_a + 'b' * count_b and count_a == count_b

#Função que aplica o lema do bombeamento
def aplicar_lema_bombeamento(w, p, linguagem_fn):
    resultados = []
    encontrou_quebra = False

    for i in range(1, p + 1):  # define  y ≠ ε
        for j in range(i + 1, len(w) + 1):
            x = w[:i]
            y = w[i:j]
            z = w[j:]

            if len(x + y) <= p:
                print(f"\nDivisão: x='{x}', y='{y}', z='{z}'")

                # Testa para i = 0, 1, 2.. Bombeia e diz se continua ou não pertencendo a linguagem
                for n in range(0, 4):
                    teste = x + y * n + z
                    pertence = linguagem_fn(teste)
                    resultados.append((teste, pertence))
                    print(f"i={n}: {teste} → {'Pertence' if pertence else 'Não pertence'} à linguagem")
                   #caso não pertença marca a quebra como verdadeira
                    if not pertence:
                        encontrou_quebra = True
    return encontrou_quebra, resultados

#Define a cadeia e o valor do bombeamento
w = 'aabb'  # |w| = 4
p = 2      # valor de bombeamento p≥|w|

#Chama as funções e apresenta se o lema foi quebrado apontando que a linguagem não é regular
quebra, testes = aplicar_lema_bombeamento(w, p, linguagem_a_n_b_n)

if quebra:
    print("\n O lema do bombeamento foi quebrado. A linguagem não é regular.")
else:
    print("\n O lema do bombeamento não foi quebrado neste caso.")
    