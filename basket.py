class BasketModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS basket 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             drug_id INTEGER,
                             user_id INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, drug_id, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO basket
                          (drug_id, user_id) 
                          VALUES (?,?)''', (str(drug_id), str(user_id)))
        cursor.close()
        self.connection.commit()


    def get_all(self, user_id):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM basket WHERE user_id = ?", (str(user_id),))
        rows = cursor.fetchall()
        return rows


    def delete(self, drug_id, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM basket WHERE drug_id = ? AND user_id = ?''', ((str(drug_id)), (str(user_id))) )
        cursor.close()
        self.connection.commit()