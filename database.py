import sqlite3


class Database:
    """Класс хранилища: сохраняет и читает данные из SQLite."""

    def __init__(self, db_name="manicure.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Создаёт таблицы, если их ещё нет."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                note TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                duration INTEGER,
                price REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                service_id INTEGER,
                date TEXT,
                time_start TEXT,
                status TEXT DEFAULT 'запланирована',
                note TEXT
            )
        """)
        self.conn.commit()

    # --- Клиенты ---

    def add_client(self, name, phone, note=""):
        """Добавляет клиента и возвращает его id."""
        if not name:
            raise ValueError("Имя клиента не может быть пустым")
        self.cursor.execute(
            "INSERT INTO clients (name, phone, note) VALUES (?, ?, ?)",
            (name, phone, note)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_clients(self):
        """Возвращает список всех клиентов."""
        self.cursor.execute("SELECT id, name, phone, note FROM clients")
        return self.cursor.fetchall()

    # --- Услуги ---

    def add_service(self, name, duration, price):
        """Добавляет услугу и возвращает её id."""
        if not name:
            raise ValueError("Название услуги не может быть пустым")
        self.cursor.execute(
            "INSERT INTO services (name, duration, price) VALUES (?, ?, ?)",
            (name, duration, price)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_services(self):
        """Возвращает список всех услуг."""
        self.cursor.execute("SELECT id, name, duration, price FROM services")
        return self.cursor.fetchall()

    # --- Записи ---

    def add_appointment(self, client_id, service_id, date, time_start,
                        status="запланирована", note=""):
        """Добавляет запись и возвращает её id."""
        self.cursor.execute(
            """INSERT INTO appointments
               (client_id, service_id, date, time_start, status, note)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (client_id, service_id, date, time_start, status, note)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_appointments_by_date(self, date):
        """Возвращает все записи на указанную дату."""
        self.cursor.execute(
            """SELECT id, client_id, service_id, date, time_start, status, note
               FROM appointments
               WHERE date = ?
               ORDER BY time_start""",
            (date,)
        )
        return self.cursor.fetchall()

    # --- Закрытие ---

    def close(self):
        """Закрывает соединение с базой."""
        self.conn.close()