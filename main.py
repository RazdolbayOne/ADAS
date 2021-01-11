import mysql.connector
from mysql.connector import Error


# import pandas as pd


def create_server_connection(host_name, user_name, user_password):
    """return conn object on succes of connecting to db
     or return none and prints error msg"""

    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def main():
    conn = create_server_connection("localhost", "root", "My3qlP@ssword")


if __name__ == "__main__":
    main()
