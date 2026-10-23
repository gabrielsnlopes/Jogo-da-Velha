# ==========================================
# Jogo da Velha
# ==========================================
# ==========================================
# Gabriel Lopes
# ==========================================

casas = list('123456789')
trios = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)]

def mostrar():
    for i in range(0, 9, 3):
        print(' | '.join(casas[i:i+3]))

def venceu():
    for a, b, c in trios:
        if casas[a] == casas[b] == casas[c]:
            return True
    return False

vez = 'X'

for rodada in range(9):
    mostrar()
    while True:
        try:
            n = int(input(f'Vez do {vez}: ')) - 1
            if n < 0 or n > 8:
                print('Escolha um número de 1 a 9.')
            elif casas[n] in 'XO':
                print('Casa ocupada.')
            else:
                break
        except ValueError:
            print('Introduza um número válido.')
    casas[n] = vez
    if venceu():
        mostrar()
        print(f'O jogador {vez} venceu!')
        break
    vez = 'O' if vez == 'X' else 'X'
else:
    mostrar()
    print('Deu velha!')