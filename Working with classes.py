class User():
 def __init__(self, first_name, last_name, nickname):
  self.first_name = first_name
  self.last_name = last_name
  self.nickname = nickname
  self.login_attempts = 0


 def describe_user(self):
   print(f'''First Name: {self.first_name},\nLast Name: {self.last_name},\nNickname: {self.nickname}.''')

 def greet_user(self):
  print(f"Wlcome to site {self.nickname}!")

 def increment_login_attempts(self):
  self.login_attempts += 1
  print(f"Login attempts {self.login_attempts}")



class Admin(User):
 def __init__(self, first_name, last_name, nickname):
  super().__init__(first_name, last_name, nickname)
  self.privileges = []

 def show_privileges(self):
   print("You'r privileges:")
   for privilege in self.privileges:
    print(f"\t*{privilege}")

#my_user1 = User("John", "Smith", "Thony")
my_admin1 = Admin("Mark", "Ten", "Administrator")
my_admin1.privileges = ["разрешено добавлятьсообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

my_admin1.describe_user()
my_admin1.show_privileges()

#my_user1.describe_user()
#my_user1.greet_user()
#my_user1.increment_login_attempts()
