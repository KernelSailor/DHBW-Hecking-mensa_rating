from backend.db.user_dao import UserDAO

dao = UserDAO()

dao.insert_user("karl.klammer@office.de", "Karl Klammer", "12345")
dao.insert_user("s.schwarz@gmx.de", "Sabine Schwarz", "sdfk§46")
dao.insert_user("will-mates@gmail.com", "Will Mates", "qwertz")

dao.delete_user("karl.klammer@office.de")

dao.insert_suggestion("s.schwarz@gmx.de", "Pizza Bianca (https://rezepte.se/....)")
user = dao.get_user("s.schwarz@gmx.de")

print(user)
