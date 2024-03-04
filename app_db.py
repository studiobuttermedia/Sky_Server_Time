from db_config import DB_CONFIG
import pymysql

def create_connection():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        print("Connected successfully!")
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

if __name__ == "__main__":
    db_connection = create_connection()
    print("Connection Created!")
    # Now you can use the connection for queries, inserts, etc.

# Example query execution
try:
    with db_connection.cursor() as cursor:
        sql = "SELECT * FROM data"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    db_connection.close()
    print('Connection Close')
