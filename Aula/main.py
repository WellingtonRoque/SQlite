from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()

	banco.inserir_cliente('wel', '11111111111', 'wel@gmail.com')
	banco.inserir_cliente('roque', '22222222222', 'roque@gmail.com')

	banco.desconecta()
