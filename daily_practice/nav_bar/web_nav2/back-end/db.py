import mysql.connector
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

def save_message(name, email, message):
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                message TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            INSERT INTO messages (name, email, message)
            VALUES (%s, %s, %s)
        ''', (name, email, message))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"MySQL error: {e}")
        return False
