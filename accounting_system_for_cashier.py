import csv


def currency() -> list[str]:
    with open('currency.csv', 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        data = [dict(row) for row in reader]
        return data


class AccountingSystem:

    def __init__(self):
        self.reader = self.read_foo()
        self.input_user = self.user_input()
        self.split_input = self.input_user.split()
        self.input_foo()

    def input_foo(self):
        if self.input_user == 'COURSE USD':
            return self.course_usd()
        elif self.input_user == 'COURSE UAH':
            return self.course_uah()
        elif self.split_input[0] == 'EXCHANGE':
            if self.split_input[1] == 'USD':
                return self.exchange_usd()
            elif self.split_input[1] == 'UAH':
                return self.exchange_uah()
            else:
                return self.some_else()
        elif self.input_user == 'STOP':
            print('SERVICE STOPPED')
        else:
            return self.some_else()

    def exchange_usd(self):
        if self.split_input[-1].isdigit():
            trade = int(self.split_input[-1]) * float(self.my_file()['rateUSD'])
            if trade <= float(self.my_file()['availableUAH']):
                self.read_foo()
                self.reader[1][1] = float(self.my_file()['availableUSD']) + int(self.split_input[-1])
                self.reader[1][3] = float(self.my_file()['availableUAH']) - trade
                self.write_foo()
                print(f'UAH {round(trade, 2)}, RATE {self.my_file()["rateUSD"]}')
                return self.__init__()
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE UAH {round(trade, 2)}, '
                      f'AVAILABLE {self.my_file()["availableUAH"]}')
                return self.__init__()
        else:
            return self.some_else()

    def exchange_uah(self):
        if self.split_input[-1].isdigit():
            trade = int(self.split_input[-1]) * float(self.my_file()['rateUAH'])
            if trade <= float(self.my_file()['availableUSD']):
                self.read_foo()
                self.reader[1][3] = round(float(self.my_file()['availableUAH']), 3) + int(self.split_input[-1])
                self.reader[1][1] = round(float(self.my_file()['availableUSD']), 3) - trade
                self.write_foo()
                print(f'USD {round(trade, 2)}, RATE {self.my_file()["rateUAH"]}')
                return self.__init__()
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE USD {round(trade, 2)}, '
                      f'AVAILABLE {self.my_file()["availableUSD"]}')
                return self.__init__()
        else:
            return self.some_else()

    def read_foo(self):
        with open('currency.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            readers = list(reader)
            while True:
                try:
                    readers.remove([])
                except ValueError:
                    break
            return readers

    def write_foo(self):
        with open('currency.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.reader)

    def some_else(self):
        if len(self.split_input) == 2 and self.split_input[0] == 'COURSE':
            print('INVALID CURRENCY ', self.split_input[1])
            return self.__init__()
        else:
            print(f'Invalid input {self.input_user}')
            return self.__init__()

    def course_uah(self):
        print(f'RATE: {self.my_file()["rateUAH"]}, AVAILABLE: {self.my_file()["availableUAH"]}')
        return self.__init__()

    def course_usd(self):
        print(f'RATE: {self.my_file()["rateUSD"]}, AVAILABLE: {self.my_file()["availableUSD"]}')
        return self.__init__()

    def my_file(self):
        for dict_ in currency():
            return dict_

    def user_input(self):
        print('COMMAND?')
        inputted = input('Input your command: ')
        return inputted.upper()


if __name__ in '__main__':
    account_sys = AccountingSystem()
