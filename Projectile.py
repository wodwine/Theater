from random import randint
import sys


class Cinema:
    def __init__(self):
        self.list_movie = []
        self.list_booking = []

    def delete_movie(self, index):
        self.list_movie.pop(index - 1)

    def get_movie(self):
        return self.list_movie

    def get_movie_by_index(self, index):
        print(f"You got {self.list_movie[index-1][0]}!!")

    def print_movie(self):
        print("Movie Summary")
        number_of_movie = 1
        for info in self.list_movie:
            print(f"{number_of_movie}. {info[0]:<12} : {info[1]} seats, Price {info[3]} bath/seat")
            number_of_movie = number_of_movie + 1

    def booking(self, name, index_movie, amount):
        for movie in self.list_movie:
            if index_movie - 1 == self.list_movie.index(movie):
                name_movie = movie[0]
                movie[2] = movie[2] - amount
        self.list_booking.append([name, name_movie, amount, movie[2], movie[2] - amount])

    def print_booking(self):
        print("Booking Summary")
        number_of_movie = 1
        for info in self.list_movie:
            print(f"{number_of_movie}. {info[0]:<12} : {info[1]} seats/Remaining : {info[2]}")
            number_of_movie = number_of_movie + 1

    def print_report(self, index, card_type):
        for movie in self.list_movie:
            if index - 1 == self.list_movie.index(movie):
                name_movie = movie[0]
                seats = movie[1]
                price = movie[3]
        number_of_movie = 1
        now_seat = 0
        for info in self.list_booking:
            if info[1] == name_movie:
                now_seat = now_seat + info[2]
        print(f"{name_movie:<12}  {seats} seats/Remaining {seats-now_seat} seats, Price {price} bath/seat")
        if card_type == "S":
            discount = price * 0.05
        elif card_type == "B":
            discount = price * 0.10
        elif card_type == "G":
            discount = price * 0.15
        else:
            discount = 0
        for info in self.list_booking:
            if info[1] == name_movie:
                print(f"{number_of_movie}.{info[0]} {info[2]} seats, Total Price: "
                      f"{((price*info[2])-(discount*info[2])):.0f} bath. "
                      f"(Discount: {discount*info[2]:.0f} bath)")
                number_of_movie = number_of_movie + 1
        print(f"  Total {now_seat} seats")

    def delete_booking(self, first_index, second_index):
        for movie in self.list_movie:
            if first_index - 1 == self.list_movie.index(movie):
                name_movie = movie[0]
        for number in range(len(self.list_booking)):
            if second_index - 1 == number and name_movie == self.list_booking[number][1]:
                seat = self.list_booking[second_index - 1][2]
                self.list_booking.pop(second_index - 1)
        for movie in self.list_movie:
            if first_index - 1 == self.list_movie.index(movie):
                movie[2] = movie[2] + seat

    def add_movie_and_capacity(self):
        file_movie = open("Movie.txt").read().splitlines()
        for info in file_movie:
            colon1 = info.find(":") + 1
            colon2 = info.find(":", colon1)
            movie = info[colon1:colon2]
            square1 = info.find("#", colon2) + 1
            square2 = info.find("#", square1)
            seat = info[square1:square2]
            asterisk1 = info.find("*", square2) + 1
            asterisk2 = info.find("*", asterisk1)
            price = info[asterisk1:asterisk2]
            self.list_movie.append([movie, int(seat), int(seat), int(price)])

    def random_movie(self):
        return randint(1, len(self.list_movie))

    def add_movie_in_file(self, name, seat, price):
        file = open("Movie.txt", "a+")
        file.write("Name:" + name + ":seat#" + str(seat) + "#price*" + str(price) + "*\n")

    def delete_movie1(self, index):
        file_movie = open("Movie.txt").read().splitlines()
        file_movie.pop(index)
        file = open("Movie.txt", "w")
        for info in file_movie:
            file.write(info + "\n")

    def update_movie(self):
        self.list_movie = []
        file_movie = open("Movie.txt").read().splitlines()
        for info in file_movie:
            colon1 = info.find(":") + 1
            colon2 = info.find(":", colon1)
            movie = info[colon1:colon2]
            square1 = info.find("#", colon2) + 1
            square2 = info.find("#", square1)
            seat = info[square1:square2]
            asterisk1 = info.find("*", square2) + 1
            asterisk2 = info.find("*", asterisk1)
            price = info[asterisk1:asterisk2]
            self.list_movie.append([movie, int(seat), int(seat), int(price)])

    def for_admin(self):
        self.add_movie_and_capacity()
        movie = self.get_movie()
        if len(movie) > 0:
            self.print_movie()
        else:
            print("No Movies")
        movie_add_word = input("(N)ew movie\n(D)elete movie\n(E)xit\nChoose a menu : ").upper()
        while movie_add_word != "E":
            if movie_add_word == "N":
                movie_name = input("Movie Name: ")
                capacity = int(input("Seat Capacity: "))
                price = int(input("Price for each seat: "))
                self.add_movie_in_file(movie_name, capacity, price)
                self.update_movie()
                self.print_movie()
            elif movie_add_word == "D":
                self.print_movie()
                index = int(input("Movie Number: "))
                self.delete_movie(index)
                self.delete_movie1(index - 1)
                self.update_movie()
                self.print_movie()
            movie_add_word = input("(N)ew movie\n(D)elete movie\n(E)xit\nChoose a menu : ").upper()
        print("Bye bye Admin")
        sys.exit()

    def cinema(self, card_type, name_member):
        print("----Menu----")
        word = input("(M)ovie\n(B)ooking\n(R)eport\n(E)xit\nChoose a menu : ").upper()
        self.add_movie_and_capacity()
        while word != "E":
            if word == "M":
                movie = self.get_movie()
                if len(movie) > 0:
                    self.print_movie()
                    movie_add_word = input("(M)ain Menu\nChoose a menu : ").upper()
                else:
                    print("No Movies")
                    movie_add_word = input("(M)ain Menu\nChosse a menu : ").upper()
                while movie_add_word != "M":
                    self.print_movie()
                    movie_add_word = input("(M)ain Menu\nChoose a menu : ").upper()
            elif word == "B":
                self.print_booking()
                movie = input("Movie or (R)andom: ")
                if movie == "R":
                    movie = self.random_movie()
                    self.get_movie_by_index(int(movie))
                elif name_member == "N":
                    name_member = input("Name: ")
                amount = int(input("Amount: "))
                self.booking(name_member, int(movie), amount)
                name_member = "N"
            elif word == "R":
                self.print_booking()
                report_word = input("Enter a movie number or (M)ain menu: ").upper()
                while report_word != "M":
                    self.print_report(int(report_word), card_type)
                    report_manage_word = input("Delete item number or (B)ack: ").upper()
                    while report_manage_word != "B":
                        self.delete_booking(int(report_word), int(report_manage_word))
                        self.print_report(int(report_word), card_type)
                        report_manage_word = input("Delete item number or (B)ack: ").upper()
                    self.print_booking()
                    report_word = input("Enter a movie number or (M)ain menu: ").upper()
            word = input("(M)ovie\n(B)ooking\n(R)eport\n(E)xit\nChoose a menu : ").upper()
        print("Have a nice day! See you soon!")
        sys.exit()

    def register_member(self):
        print("This is Member card types\n"
              "1.Silver member: has 5% discount every movie. First register Price: 300 bath\n"
              "2.Blue member: has 10% discount every movie. First register Price: 500 bath\n"
              "3.Gold member: has 15% discount every movie. First register Price: 800 bath")
        name = input("What is your name?: ")
        gender = input("Your gender(Male/Female): ")
        type_card = input("Select your card: (S)ilver, (B)lue , (G)old: ").upper()
        num = randint(10000, 100000)
        file_check = open("Member.txt", "a+").read()
        file = open("Member.txt", "a+")
        while file_check.find(str(num)) != -1:
            num = randint(10000, 100000)
        file.write("No." + str(num) + " Name:" + name + ", gender= " + gender + "#" + type_card + "*" + "\n")
        if gender == "Female":
            print(f"This is your member card number: {num}, Mrs.{name}. Thank you for register")
        elif gender == "Male":
            print(f"This is your member card number: {num}, Mr.{name}. Thank you for register")
        else:
            print(f"This is your member card number: {num}, {name}. Thank you for register")
        return str(num)

    def check_ID(self, ID):
        file_check = open("Member.txt").read()
        index = file_check.find(ID)
        comma = file_check.find(",", index)
        if index != -1 and len(ID) == 5:
            equal = file_check.find("=", index)
            square = file_check.find("#", index)
            name = file_check[index + 11:comma]
            gender = file_check[equal + 2:square]
            asterisk = file_check.find("*", index)
            card_type = file_check[square + 1:asterisk]
            if gender == "Male":
                print(f"Hello, Mr.{name}")
            elif gender == "Female":
                print(f"Hello, Mrs.{name}")
            else:
                print(f"Hello, {name}")
            return True, card_type, name
        else:
            return False, "", ""


Cinema().add_movie_and_capacity()
cinema = Cinema()
print(f"\t\t\t\tWelcome to Wine's Theater")
check_member = input("Are you a VIP member of this theater? [(Y)es/(N)o/(E)xit/(A)dmin]: ").upper()
while check_member != "E":
    if check_member == "N":
        check_register = input("Do you want to register? [(Y)es/(N)o/(E)xit]: ").upper()
        if check_register == "Y":
            ID = cinema.register_member()
            condition, card_type, name = cinema.check_ID(ID)
            cinema.cinema(card_type, name)
        elif check_register == "N":
            cinema.cinema("N", "N")
        elif check_register == "E":
            print("Have a nice day! See you soon!")
            sys.exit()
    elif check_member == "Y":
        ID = input("You're already a member, what is your ID: ")
        condition, card_type, name = cinema.check_ID(ID)
        while not condition:
            ID = input("Your ID is wrong, please type again: ")
            condition, card_type, name = cinema.check_ID(ID)
        cinema.cinema(card_type, name)
    elif check_member == "A":
        Cinema().for_admin()
    else:
        print(f"You typed wrong! Please retype again")
        check_member = input("Are you a VIP member of this theater? [(Y)es/(N)o/(E)xit/(A)dmin]: ").upper()
print("Have a nice day! See you soon!")
