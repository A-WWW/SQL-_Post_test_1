from psycopg2 import OperationalError
import psycopg2
from Config import host, user, password, db_name
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE friends(
    #         id serial  PRIMARY KEY,
    #         first_name varchar(30) NOT NULL,
    #         second_name varchar(30) NOT NULL,
    #          street varchar(30) NOT NULL,
    #          code_name varchar(30));"""
    #     )
    #     print("[INFO] Tabl created")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO friends (first_name, second_name, street) VALUES
    #         ('George', 'Clooney', 'Street_1'),
    #          ('George', 'Lucas', 'Street_2'),
    #           ('George', 'Michael', 'Street_3');"""
    #     )
    #     print("[INFO] Date wos succefully")

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT second_name FROM friends  WHERE street = 'Street_2';"""
          )
        print(cursor.fetchone())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE friends;"""
    #       )
    #     print("[INFO] Tabl wos deleted")

except Exception as _ex:
    print("(INFO) Error wile", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] conection clossed")
