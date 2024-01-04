# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('João', 11)


with open(r'D:\projects\curso_python\secao5 - introducao a POO com Python - Classes\aula127\aula127_classe.json', 'w', encoding='utf8') as arquivo:
    json.dump(Pessoa.__dict__,
              arquivo,
              ensure_ascii=False,
              indent=4
              )

with open(r'D:\projects\curso_python\secao5 - introducao a POO com Python - Classes\aula127\aula127_instancia.json', 'w', encoding='utf8') as arquivo:
    json.dump(p1.__dict__,
              arquivo,
              ensure_ascii=False,
              indent=4
              )
