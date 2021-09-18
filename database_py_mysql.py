import mysql.connector as sql 

conex = sql.connect(
    host ="localhost",
    user = "root",
    port = 3306,
    database= 'cadastro',
    password= '')

if conex.is_connected():

    db_info = conex.get_server_info()

    print('Conectado ao servidor MySQL versão',db_info)

    cursor = conex.cursor()

    cursor.execute( "select database();")

    linha= cursor.fetchone()

    print ("Conectado ao banco de dados", linha)

if conex.is_connected():

   cursor.close()

   conex.close()

   print("A Conexão ao MySQL foi encerrada")


