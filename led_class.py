class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, number):
        self.number = number    # instance variable unique to each instance
    
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.number                  # unique to d
'Fido'
>>> e.number                  # unique to e
'Buddy'