class Player:
    def __init__(self, name, corses):
        self.name = name
        self.corses = corses
        self.dict = [self.name, self.corses]
        self.corses_app = {}
        

    def open_students(self):
        print(self.dict[0], '- курс', self.dict[1])
        print('say hello')
        return

    def task(self, student):
        pass

    def add_corses(self, new_corses, student, grade):
        pass
        

        
student = Player('Igor', 'p-66')

student.open_students()

