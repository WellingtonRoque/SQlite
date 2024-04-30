from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()

	"""  CHAMADA DOS METODOS """

	"""Criar tabelas"""
	banco.criar_tabelas()

	"""Inserir Clientes"""
	#banco.inserir_cliente("wel","11111111111","wel@gmail.com")
	#banco.inserir_clientes("roque","22222222222","roque@gmail.com")

	"""Buscar Clientes"""
	banco.buscar_cliente('11111111111')

	banco.desconecta()


	""" Burcar cliente pelo email """

	""" REMOVER cliente pelo cpf """

