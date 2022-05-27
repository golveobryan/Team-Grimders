import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=C:\Users\bryan\OneDrive\Documents\Database1.xlsx;',autocommit=True)
    print("Database is connected")

data.execute("Insert From Database1")
Inventor = "Larry Page"
Invention = "Google"
DateofInvention = "1998"
Description = "An American computer scientist and internet entrepreneur. He is best known as one of the co-founders of Google, along with Sergey Brin." ID = 8

record = connect.cursor()

connection.commit()
    print('Database inserted')

except pyodbc.Error as e:
    print("Connection Error")
