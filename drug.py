class DrugModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS drug 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             name VARCHAR(100),
                             discrip VARCHAR(1000),
                             number VARCHAR(100),
                             user_id INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, name, discrip, number, user_id):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO drug 
                          (name, discrip,number, user_id) 
                          VALUES (?,?,?,?)''', (name, discrip, number, str(user_id)))
        cursor.close()
        self.connection.commit()

    def get(self, drug_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM drug WHERE id = ?", (str(drug_id)))
        row = cursor.fetchone()
        return row

    def get_all(self, user_id=None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM drug WHERE user_id = ?", (str(user_id),))
        else:
            cursor.execute("SELECT * FROM drug")
        rows = cursor.fetchall()
        return rows


    def delete(self, drug_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM drug WHERE id = ?''', (str(drug_id)))
        cursor.close()
        self.connection.commit()

    def update(self, drug_id, n=1):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM drug WHERE id = ?", (str(drug_id)))
        row = cursor.fetchone()
        num = int(row[3])-n
        cursor.execute('''UPDATE drug SET number = :num WHERE id = :id ''', {'num': num, 'id': (str(drug_id))})
        cursor.close()
        self.connection.commit()
