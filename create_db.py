from db import DB
from user import UserModel
from drug import DrugModel
from basket import BasketModel


db = DB()
users_model = UserModel(db.get_connection())
users_model.init_table()
users_model.insert("admin", "admin")
news_model = DrugModel(db.get_connection())
news_model.init_table()
basket_model = BasketModel(db.get_connection())
basket_model.init_table()
