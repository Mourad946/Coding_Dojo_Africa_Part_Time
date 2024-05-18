class User:
    #! constructor
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    #! display_info Methods
    # display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print("User Information:")
        print(f"First Name: {self.first_name}\n")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {'Yes' if self.is_rewards_member else 'No'}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self

    #! enroll methods
    # Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
    def enroll(self):
        if self.is_rewards_member:
            print(f"❌❌❌ User already a member ❌❌❌")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"✅✅✅ Enrolled Successfully ✅✅✅\n The new Gold Card Points the enrolled user is: {self.gold_card_points}")
            return self
    #! spend methods
    # Implement the spend_points(self, amount) method
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"❌❌❌ Not enough points.\n You have {self.gold_card_points} points and tried to spend {amount} points. ❌❌❌")
        else:
            self.gold_card_points -= amount
            # self.gold_card_points = self.gold_card_points - amount
            print(f"Spent {amount} points succesfully.\n New Balance is {self.gold_card_points} points")
        return self 

# In the outer scope, create a user instance and call the display_info method to test.
user_1 = User("John", "Doe", "john@gmail.com", 30)

#! Make 2 more instances of the User class.
user_2 = User("Jane", "Smith", "jane@gmail.com", 20)
user_3 = User("Mourad", "Thlijeni", "mouradthlijeni@gmail.com", 30)

#! Test display_info method for this instance
# user_1.enroll()
# user_1.spend_points(50)
# print("--"*20)
# user_2.enroll()
# user_2.spend_points(70)
# print("--"*20)
# user_3.enroll()
# user_3.spend_points(160)

#! Test display_info method after enroll and spend_points for each instance
# print("--"*20)
# print(f"Users Informations after Spend Points and Enroll")
# user_1.display_info()
# print("--"*20)
# user_2.display_info()
# print("--"*20)
# user_3.display_info()

#! BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
# user_1.enroll()
# print("--"*20)
# user_1.enroll()

#! BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
# user_3.enroll()
# user_3.spend_points(40)
# user_3.display_info()

#! Chaining methods
user_1.enroll().spend_points(40).spend_points(50).spend_points(10).display_info()