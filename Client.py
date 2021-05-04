class Client:

    def __init__(self, name, phone, address, point, time, index):
        self.name = name
        self.phone = phone
        self.address = address
        self.point = point
        self.index = index
        self.time = time
        self.distanceToPoint = []

    def __lt__(self, other):
        if self.time < other.time:
            return True
        if self.time == other.time:
            return self.name < other.name
        return False

    def __str__(self):
        return 'Заказчик: ' + self.name \
                   + '\n' + 'Номер телефона: ' \
                   + self.phone + '\n' \
                   + '\n \n' \
                   + 'https://yandex.ru/navi/?whatshere%5Bpoint%5D=' \
                   + self.point[1] + '%2C' + self.point[0] \
                   + '&whatshere%5Bzoom%5D=18&lang=ru&from=navi' + '\n'
