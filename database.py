import mysql.connector

DataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "imrankhan",
    database = "final"
)

if DataBase.is_connected():
    print("Succesfully connected!")

    cursor = DataBase.cursor()

    query = "Select * from books"

    cursor.execute(query)

    result = cursor.fetchall()

    for rows in result:
        print(rows)

else:
    print("Not Connected!")