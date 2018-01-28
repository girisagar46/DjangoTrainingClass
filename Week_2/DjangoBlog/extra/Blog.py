import datetime

class Blog:
    def __init__(self, author, title, text):
        self.author = author
        self.title = title
        self.text = text
        self.created_date = datetime.datetime.now()
        self.publish_date = datetime.datetime.now()

    def publish(self):
        self.publish_date = datetime.datetime.now()

    def __str__(self):
        return f"{self.__dict__}"


b1 = Blog("Sagar", "Python 101", "Python is awesome")
b2 = Blog("Sagar Giri", "Django 101", "Django is awesome")

print(b1)
print(b2)

b1.publish()
b2.publish()

print(b1)
print(b2)