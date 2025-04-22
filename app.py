from backend.db.user_dao import UserDAO

dao = UserDAO()

dao.insert_user("karl.klammer@office.de", "Karl Klammer")
dao.insert_user("s.schwarz@gmx.de", "Sabine Schwarz")

user = dao.get_user("s.schwarz@gmx.de")

print(user)
