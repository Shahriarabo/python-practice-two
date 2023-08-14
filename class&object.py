class rasel:
    name = ""
    number = ""


a = rasel()
a.name = "Abdulla al shahriar"
a.number = "01650088493"

print(a.name)
print(a.number)


class user(object):
    count = 0
    def __init__(self,name,age):
        self.name= name
        self.age = age
        self.count = user.count + 1

    @staticmethod
    def hello():
        print("Hello Wrold")

    @classmethod
    def get_count(cls):
        return cls.count

u.user("ak","22")
y.user("ak","22")

 print user.get_count



u = user("Abdullah ","20")
u = user(" Al Shahriar","20")
u = user("Abdullah Al ","20")
u = user(" Shahriar","20")
y = user("Abdullah ","22")
print(u.count)

y = user("Abdullah ","22")
print(y.count)

