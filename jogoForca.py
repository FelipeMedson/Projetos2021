# Jogo da Forca
# Programação Orientada à Objetos


import random

forca = ['''
>>>>>>>Jogo da Forca - Boa Sorte!<<<<<

    -------
    |     |  
    |
    |
    |
    |
  ====== ''','''
    -------
    |     |     
    |     O  
    |
    |
    |
  ====== ''','''
    -------
    |     |     
    |     O  
    |     |
    |
    |
  ====== ''','''
    -------
    |     |     
    |     O  
    |    /|
    |
    |
  ====== ''','''
    -------
    |     |     
    |     O  
    |    /|\ 
    |
    |
  ====== ''','''
    -------
    |     |     
    |     O  
    |    /|\ 
    |    /
    |
  ====== ''','''
    -------
    |     |     
    |     O  
    |    /|\ 
    |    / \ 
    |
  ====== ''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        print(forca[0])
        self.word = word
        self.corretas = []
        self.erradas = []
        print(self.hide_word())

    # Método para adivinhar a letra
    def guess(self, letter):

        if letter in self.word and letter not in self.corretas:
            self.corretas.append(letter)

        elif letter not in self.word and letter not in self.erradas:
            self.erradas.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.erradas) == 6)

    # Método para não mostrar a letra no board
    def hide_word(self):
        palavra = ''
        for letter in self.word:
            if letter not in self.corretas:
                palavra += ' _'
            else:
                palavra += letter
        return palavra

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(forca[len(self.erradas)])
        print(self.hide_word())
        print("Letras erradas:", self.erradas)
        print("Letras corretas:", self.corretas)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("C:/PythonFundamentos/Cap05/Lab03/palavrasAleatorias.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


def main():
    # Objeto
    game = Hangman(rand_word())
    print('DICA: A palavra é uma fruta!')

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        letter = input("Digite uma letra: ")
        game.guess(letter)

        # Verifica o status do jogo
        game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()
