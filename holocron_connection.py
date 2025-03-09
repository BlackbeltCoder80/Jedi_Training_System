import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="BlackBeltCoder#1980", # Used to sign into SQL Data Base
        database="Jedi_Training_db"
    )