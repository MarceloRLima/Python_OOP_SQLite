#Importar nosso arquivo Pessoa.y no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
marcelo = Pessoa (1, "Marcelo Lima")
print(marcelo)

#Quero mostrar só o nome
print(marcelo.nome)


