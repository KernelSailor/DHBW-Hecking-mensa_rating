from backend.db.user_dao import UserDAO

dao = UserDAO()

dao.insert_user("tobias.hecking@dlr.de", "Tobias Hecking")
dao.insert_user("s.schwarz@gmx.de", "Sabine Schwarz")

user = dao.get_user("tobias.hecking@dlr.de")

user = dao.get_user("s.schwarz@gmx.de")

print(user)
