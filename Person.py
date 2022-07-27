import random

class Person:
    def __init__(self, id, gender,n):
        self.p_list = []
        #function to create a random list of preferences
        for i in range(0,n):
            self.p_list.append(i)
        random.shuffle(self.p_list)
        self.id = id
        self.gender = gender
        self.preferences = self.p_list
        self.available_proposals = list(self.preferences)
        self.partner = None


    def get_preference(self, y):
        #index of one gender with respect to other
        return self.preferences.index(y)

    


