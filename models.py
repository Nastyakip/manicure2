class Clients:
    def __init__(self, id, name, phone, note):
        self.id = id
        self.name = name
        self.phone = phone
        self.note = note

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'note': self.note
        }
clients1 = Clients(1, 'Мария', '+7 925 000 00 00', 'Аллергия на лак люксио')#вызов класса

class Service:
    def __init__(self, id, name, duration, price):
        self.id = id
        self.name = name
        self.duration = duration
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'price': self.price
        }
service1 = Service( 1, 'классический маникюр', 60, 1000)



class Appointment:
    def __init__(self, id=None, client_id=None, service_id=None,
                 date="", time_start="", status="запланирована", note=""):
        self.id = id
        self.client_id = client_id
        self.service_id = service_id
        self.date = date
        self.time_start = time_start
        self.status = status
        self.note = note

    def to_dict(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'service_id': self.service_id,
            'date': self.date,
            'time_start': self.time_start,
            'status': self.status,
            'note': self.note
        }

appointment1 = Appointment(
    1,
    clients1.id,
    service1.id,
    '2025-05-20',
    '14:00',
    'запланирована',
    'Первый визит'
)

print(clients1.to_dict())
print(service1.to_dict())
print(appointment1.to_dict())


