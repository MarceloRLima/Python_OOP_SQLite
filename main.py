#Importar nosso arquivo Pessoa.y no diretório model
from model.Pessoa import Pessoa
from basedados.BaseDados import BaseDados
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
marcelo = Pessoa (1, "Marcelo Lima")
print(marcelo)

#Quero mostrar só o nome
print(marcelo.nome)

print("\nDAQUI PRA FRENTE É ACESSO AO BANCO...\n")

#Chama o objeto de banco de dados
db = BaseDados()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)


#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(0, "Denzel Washington")

#Olha que simples...
novo = pessoaDAO.save (novo)

#consulta o banco de novo..
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)