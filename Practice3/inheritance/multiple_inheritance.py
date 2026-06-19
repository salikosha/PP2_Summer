class Father:
    def skills_father(self):
        print("Father: I can play football")

class Mother:
    def skills_mother(self):
        print("Mother: I can sing a song")

class Child(Father, Mother):
    def skills_child(self):
        print("Child: I can learn from both parents")

c = Child()

c.skills_father()
c.skills_mother()
c.skills_child()
