DEBUG = True      #podemos alterar o arquivo e ele atualiza sozinho, sem precisar reiniciar o servidor (ctrl+C e inicializar de novo).

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'  # URI de conexao com o banco de dados,ou seja, o caminho que passar até o banco de dados (estabelecer a conexão)
SQLALCHEMY_TRACK_MODIFICATIONS = True    #acabar com o warming
