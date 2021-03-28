class Quiz:
    def __init__(self):
        self.contador = 0

    def cacecalho_jogo(self):
        print("****************")
        print("    QUIZ O_O    ")
        print("****************")

    def perguntas(self):
        abre_arquivo = open("perguntas.txt", "r")
        perguntas = abre_arquivo.readlines()
        return perguntas

    def respostas(self):
        abre_arquivo = open("resposta.txt", "r")
        resposta_correta = abre_arquivo.readlines()
        return resposta_correta

    def gera_quiz(self,perguntas,resposta_correta):
        acertou = 0
        errou = 0
        while self.contador >= 0 and self.contador <= len(perguntas)-1:
            perg = input(perguntas[self.contador])
            if perg == resposta_correta[self.contador].strip():
                print("Acertou!")
                acertou +=1
            else:
                print("Errou!")
                errou += 1

            self.contador += 1 # Verifica a Rodada

        else:
            print("Fim do Quiz")
            print(f"Você Acertou {acertou} resposta(s)! e Errou {errou} resposta(s)!")

q = Quiz()
q.cacecalho_jogo()
q.gera_quiz(q.perguntas(),q.respostas())