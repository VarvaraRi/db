class UserModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password VARCHAR(12)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password) 
                          VALUES (?,?)''', (user_name, password))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ? AND password = ?", (user_name, password))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)
