import pymysql
import pymysql.cursors
class DBConnector:
	__instance = None

	def __init__(self):
		
		DBConnector.__instance = pymysql.connect(
        	host = '192.168.56.101',
			user = 'admin',
			password = 'admin123',
			db = 'tarefas',
			charset='latin1',
        	cursorclass=pymysql.cursors.DictCursor
        )

	def get_connection():
		if(DBConnector.__instance == None):
			DBConnector()
		return DBConnector.__instance



class GerenciadordeTarefas:


	def inserir_dados(self):

		sql = "INSERT INTO tarefas.Tarefas(nome,descricao,data_conclusao,prioridade,foi_concluido) VALUES ('%s','%s','%s',%d,%d)"

		nome = input("Digite o nome da tarefa \n")
		descricao = input("Digite a descricao da tarefa \n")
		data_conclusao = input("Digite a data de conclusao da tarefa yyyy-MM-dd HH:mm:ss\n")
		prioridade = input("Digite a prioridade da sua tarefa essa podendo ser ate 11 \n")
		sql = sql % (nome, descricao, data_conclusao, int(prioridade), 0)

		con = DBConnector.get_connection()
	def mostrar_tarefas(self):
		sql = "SHOW DATABASES"	

		with con:
			cursor = con.cursor()
			cursor.execute(sql)


gerenciador = GerenciadorTarefas()
gerenciador.inserir_dados()
