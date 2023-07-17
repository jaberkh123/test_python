import mysql.connector
from mysql.connector import Error
from datetime import datetime

def to_date(timestamp):
     return datetime.fromtimestamp(int(timestamp))


def get_data_by_date(start_date, end_date):
    try:
        connection = mysql.connector.connect(user='user', password='pass', host='localhost', port=3306, database='data_baes')
        mycursor = connection.cursor()

        sql = "SELECT * FROM data2 WHERE query_date BETWEEN %s AND %s"
        val = (start_date, end_date)
        mycursor.execute(sql, val)
        records = mycursor.fetchall()

        mycursor.close()
        connection.close()

        return records

    except Exception as e:
        print(f"Error while fetching data from database: {e}")
        return False

def add_db(triples):
    try:
        connection = mysql.connector.connect(user='user', password='pass', host='localhost', port=3306, database='data_baes')
        mycursor = connection.cursor()

        sql = "INSERT INTO data (query_date, name, num) VALUES (%s, %s, %s)"
        val = [(to_date(triple[0]), triple[1], triple[2]) for triple in triples]
        mycursor.executemany(sql, val)
        connection.commit()

        mycursor.close()
        connection.close()

        print('Connection to MySQL database closed')
        return True

    except Exception as e:
        print(f"Error while inserting data into database: {e}")
        return False



