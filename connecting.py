import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=C:\Users\bryan\OneDrive\Documents\Database1.xlsx;',autocommit=True)
    print("Database is inserted")



except pyodbc.Error as e:
    print("Error in Connection")