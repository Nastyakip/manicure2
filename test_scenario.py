from database import Database

# 1. Подключаемся к базе (создастся файл manicure.db)
db = Database()

# 2. Добавляем клиента
try:
    client_id = db.add_client("Мария", "+7 925 000 00 00", "Аллергия на лак")
    print(f"✔ Добавлен клиент, id = {client_id}")
except ValueError as e:
    print(f"⚠ Ошибка: {e}")

# 3. Проверяем ошибку: пустое имя
try:
    db.add_client("", "+7 000 000 00 00")
    print("Ошибка не сработала — плохо")
except ValueError as e:
    print(f"✔ Проверка работает: {e}")

# 4. Показываем всех клиентов
print("\nСписок клиентов:")
for row in db.get_all_clients():
    print(row)

# 5. Закрываем базу
db.close()в