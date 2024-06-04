from datetime import datetime


class Operation:
    count = 0

    def __init__(self, src_collection):
        self.src = src_collection
        self.description = self.src["description"]
        self.amount = self.src["operationAmount"]["amount"]
        self.currency = self.src["operationAmount"]["currency"]["name"]
        self.num = ""
        self.sender = ""
        self.get_sender()
        self.receiver = ""
        self.get_receiver()
        self.date = ""
        self.get_date()
        type(self).count += 1

    def get_sender(self):
        self.sender = self.src.get("from")
        if self.sender:
            self.sender = self.num_transform(self.sender)
        else:
            self.sender = "Источник не определен"
        return self.sender

    def get_receiver(self):
        self.receiver = self.num_transform(self.src.get("to"))
        return self.receiver

    def num_transform(self, num_full):
        self.num = num_full.split()
        n = self.num.pop(-1)
        if len(n) == 16:
            n = f'{n[0:4]} {n[4:6]}** **** {n[12:]}'
            self.num.append(n)
            return " ".join(self.num)
        else:
            n = f'**{n[-4:]}'
            self.num.append(n)
            return " ".join(self.num)

    def get_date(self):
        date_src = datetime.fromisoformat(self.src["date"])
        self.date = datetime.strftime(date_src, "%d.%m.%Y")
        return self.date

    def __repr__(self):
        return f'show transactions with special output formatting'


if __name__ == "__main__":
    pass
