class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day},{type(month), month},{type(year), year}"
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def valid(data):

            int_data = [int(i) for i in data.split('-')]
            # date(int(year), int(month), int(day))
            if int_data[1]<= 12:
            # elif int_data[0]<= 31:
            # day, month, year = data.split('-')
            # date(int(year), int(month), int(day))
               print( 'Есть такая дата!')
            else:

               print('Указана неправильная дата!')

d = Data('26-16-1981')

print(d.type('26-12-1981'))
print(d. valid('26-16-1981'))