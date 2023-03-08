class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    # method: display info
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    # method: enroll
    def enroll(self):
        if(self.is_rewards_member == False):
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print('User is already enrolled')
        return self
    # method: spend_points
    def spend_points(self, amount):
        if(amount < self.gold_card_points):
            self.gold_card_points -= amount
        else:
            print('Insufficient Balance')
        return self

user_pavelka = User('Jacob', 'Pavelka', 'jacob.pavelka.13@gmail.com', 25)
user_franco = User('Jeremy', 'Franco', 'jeremy@gmail.com', 23)
user_sonora = User('Sally', 'Sonora', 'sally@gmail.com', 43)

user_pavelka.enroll().display_info().spend_points(50)
user_franco.enroll().spend_points(80)
user_sonora.gold_card_points = 40
user_sonora.spend_points(50)