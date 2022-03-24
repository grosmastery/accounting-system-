import csv


def currency() -> list[str]:
    with open('currency.csv', 'r', encoding='utf8') as f:
        # fieldnames = ['rateUSD', 'availableUSD', 'rateUAH', 'availableUAH']
        # reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        reader = csv.DictReader(f)
        data = [dict(row) for row in reader]
        return data


class AccountingSystem:

    def __init__(self):
        while True:
            self.input_foo()

    def input_foo(self):
        self.user_input().upper()
        print('tyt problema?')
        if self.user_input == 'COURSE USD': # ?? шо не так    :(
            print('mb tyt problema')
            return self.course_usd()
        elif self.user_input == 'COURSE UAH':
            return self.course_uah()
        elif self.user_input == 'STOP':
            return None
        else:
            return self.course_else()

    def course_else(self):
        self.user_input().split()
        if len(self.user_input()) == 2 and self.user_input()[0] == 'COURSE':
            print('INVALID CURRENCY ', self.user_input()[1])
            return self.__init__()
        else:
            print(f'Invalid input {self.user_input()}')
            return self.__init__()

    def course_uah(self):
        for dict_ in currency():
            print(f'RATE: {dict_["rateUAH"]}, AVAILABLE: {dict_["availableUAH"]}')
        return self.__init__()

    def course_usd(self):
        for dict_ in currency():
            print(f'RATE: {dict_["rateUSD"]}, AVAILABLE: {dict_["availableUSD"]}')
            if self.user_input() == 'COURSE USD':
                print('rabotaesh?')
        return self.__init__()

    def user_input(self):
        print('COMMAND?')
        # inputer = input('Input your command: ')
        return input('Input your command: ')

if __name__ in '__main__':
    account_sys = AccountingSystem()
