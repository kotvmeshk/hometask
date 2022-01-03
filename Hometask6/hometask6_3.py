class Workers:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage":int(wage), "bonus":int(bonus)}
class Position (Workers):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__( name, surname, position, wage, bonus)
    def getname(self):
        return f'{self.name}  {self.surname}'
       # " return (self.name)"
    def tot_income (self):
        return self.income["wage"]+self.income["bonus"]
a = Position ('Aleksey', 'Kovalchuk', 'editor',40000, 30000 )
print(a.getname())
print (a.tot_income())

