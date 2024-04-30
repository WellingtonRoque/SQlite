import sqlite3

class BancoDeDados:
	"""Classe que representa o banco de dados (database) da aplicação"""

	def __init__(self, nome='banco.db'):
		self.nome, self.conexao = nome, None

	def conecta(self):
		"""Conecta passando o nome do arquivo"""
		self.conexao = sqlite3.connect(self.nome)

	def desconecta(self):
		"""Desconecta do banco"""
		try:
			self.conexao.close()
		except AttributeError:
			pass

	"""  CRIAR TABELA """
	def criar_tabelas(self):
		cursor = self.conexao.cursor()
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS clientes (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			nome TEXT NOT NULL,
			cpf VARCHAR(11) UNIQUE NOT NULL,
			email TEXT NOT NULL
		);
		""")

	"""Inserir cliente no BD"""
	def inserir_cliente(self, nome, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()

			try:
				cursor.execute("""
					INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
				""",(nome, cpf, email))
			except sqlite3.IntegrityError:
				print("O cpf %s já existe" % cpf)

			self.conexao.commit()

		except AttributeError:
			print("Faça a conexão com banco antes de inserir clientes")

	""" Busca cliente no BD - cpf """
	def buscar_cliente(self, cpf):
		try:
			cursor = self.conexao.cursor()
			#obtém todos os dados
			cursor.execute("""SELECT * FROM clientes;""")

			for linha in cursor.fetchall():
				if linha[2] == cpf:
					print("Clinte %s encontrado" % linha[1])
					break
		except AttributeError:
			print("Faça aaaaa conexão com o banco antes de buscar cliente")




