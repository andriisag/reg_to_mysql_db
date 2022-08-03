import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                         database="test",
                                         user="",
                                         password = ""
)



cursor = connection.cursor()


username = input("Enter username: ")
password = input("Enter password: ")
result = input("Login or sign up(l/s): ")

sqlu = (f"SELECT name FROM login WHERE name='{username}'")
sqlp = (f"SELECT password FROM login WHERE password='{password}'")
def login(result):
  if result == "l":
    if cursor.execute(sqlu) is None and cursor.execute(sqlu) is None:
     print("Try to register")  
    else:
        print('You logged in')
  if result == "s":
   cursor.execute(f"insert into login (name, password) values ('{username}', '{password}')")
   print('You have registred')


login(result)

cursor.execute("SELECT * FROM login")
data = cursor.fetchall()


cursor.close()