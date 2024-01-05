# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = r'D:\projects\curso_python\secao5 - introducao a POO com Python - Classes\aula127\aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('João', 11)
pessoas = [p1.__dict__, vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(pessoas, arquivo,
                  ensure_ascii=False,
                  indent=4
                  )


if __name__ == '__main__':
    print('Ele é o MAIN')
    fazer_dump()
