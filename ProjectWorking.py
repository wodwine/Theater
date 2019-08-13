from tkinter import *
from tkinter import messagebox
from random import randint


class first_page:
    def on_click(self, e):
        selected = e.widget["text"]
        file = open("Score.txt", "a+")
        file.write(selected)

    def winfirstup(self, e):
        self.window1.deiconify()

    def winfirstdown(self):
        self.window1.withdraw()

    def winregisterup(self, e):
        self.window4.deiconify()

    def winregisdown(self):
        self.window4.withdraw()

    def winregisdown2(self, e):
        self.window4.withdraw()

    def winloginup(self, e):
        self.window3.deiconify()

    def winlogindown(self):
        self.window3.withdraw()

    def winlogindown2(self, e):
        self.window3.withdraw()

    def winrateup(self, e):
        self.window2.deiconify()

    def winratedown(self, e):
        self.window2.withdraw()

    def back_to_first(self, e):
        self.window5.withdraw()
        self.window1.deiconify()

    def win6up(self, e):
        self.window6.deiconify()

    def win6down(self, e):
        self.window6.withdraw()

    def win7up(self, e):
        self.window7.deiconify()

    def win7down(self, e):
        self.window7.withdraw()

    def win8up(self, e):
        self.window8.deiconify()

    def win8down(self, e):
        self.window8.withdraw()

    def win9up(self, e):
        self.card_type.set("")
        self.client_name.set("")
        self.window9.deiconify()

    def win9down(self, e):
        self.window9.withdraw()

    def win8downandwin7up(self, e):
        self.window8.withdraw()
        self.window7.deiconify()

    def win7downandwin8up(self, e):
        self.window7.withdraw()
        self.window8.deiconify()

    def Exit(self, e):
        status = messagebox.askyesno(title="Exit", message="Do you want to exit?")
        if status == 1:
            messagebox.showinfo(title="Exit", message="See you soon!")
            sys.exit()

    def rating_result(self, e):
        file = open("Score.txt").read()
        vd_num = file.count("a")
        d_num = file.count("b")
        n_num = file.count("c")
        g_num = file.count("d")
        vg_num = file.count("e")
        messagebox.showinfo(title="Exit", message=f"Very disappoint: {vd_num}\nDisappoint: {d_num}\n"
                                                  f"Normal: {n_num}\nGood: {g_num}\nVery Good: {vg_num}")

    def find_id(self, ID):
        if ID != "" and len(ID) == 5:
            file_check = open("Member.txt").read()
            index = file_check.find(ID)
            comma = file_check.find(",", index)
            if index != -1:
                equal = file_check.find("=", index)
                square = file_check.find("#", index)
                name = file_check[index + 11:comma]
                gender = file_check[equal + 2:square]
                asterisk = file_check.find("*", index)
                card_type = file_check[square + 1:asterisk]
                if gender == "Male":
                    messagebox.showinfo(title="Login Success", message=f"Hello, Mr.{name}")
                elif gender == "Female":
                    messagebox.showinfo(title="Login Success", message=f"Hello, Mrs.{name}")
                else:
                    messagebox.showinfo(title="Login Success", message=f"Hello, {name}")
                self.card_type.set(card_type)
                return True, card_type, name, gender
            else:
                messagebox.showwarning(title="ID Wrong", message=f"Your ID is wrong, please type again")
                return False, "", "", ""
        else:
            messagebox.showwarning(title="ID Wrong", message=f"Your ID is wrong, please type again")
            return False, "", "", ""

    def click(self, e):
        account = self.ID.get()
        condition, card_type, name, gender = self.find_id(account)
        self.client_name.set(name)
        if gender == "Male":
            self.client_name2.set("Welcome: Mr." + self.client_name.get())
            self.gender2.set("Male_logo.png")
        elif gender == "Female":
            self.client_name2.set("Welcome: Mrs." + self.client_name.get())
            self.gender2.set("Female_logo.png")
        self.card_type.set(card_type)
        if not condition:
            # self.winlogindown()
            self.ID.set("")
        else:
            self.winlogindown()
            self.winfirstdown()
            self.ID.set("")
            self.window5.deiconify()

    def register(self, e):
        name = self.client_name.get()
        gender = self.gender.get()
        type_card = self.card_type.get()
        num = randint(10000, 100000)
        file_check = open("Member.txt", "a+").read()
        file = open("Member.txt", "a+")
        while file_check.find(str(num)) != -1:
            num = randint(10000, 100000)
        if name != "" and (gender == "Male" or gender == "Female") and \
                (type_card == "S" or type_card == "B" or type_card == "G"):
            file.write("No." + str(num) + " Name:" + name + ", gender= " + gender + "#" + type_card + "*" + "\n")
            if gender == "Female":
                messagebox.showinfo(title="Help",
                                    message=f"Your member card: {num}, Mrs.{name}. Thank you for register")
            elif gender == "Male":
                messagebox.showinfo(title="Help", message=f"Your member card: {num}, Mr.{name}. Thank you for register")
            else:
                messagebox.showinfo(title="Help", message=f"Your member card: {num}, {name}. Thank you for register")
            self.winregisdown()
        else:
            messagebox.showwarning(title="Something Wrong", message=f"You typed wrong, please type again!")
        self.gender.set("")
        self.client_name.set("")
        self.card_type.set("")
        return str(num)

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

    def add_movie_for_show(self):
        for info in self.list_movie:
            self.movie_show.append(info[0])

    def get_gender(self):
        return self.gender.get()

    def booking(self, e):
        name = self.selected.get()
        index = self.movie_show.index(name)
        remain = self.list_movie[index][2]
        if int(self.seat.get()) > 0 and int(self.seat.get()) <= remain:
            messagebox.showinfo(title="Success", message=f"Your seat was reserved!")
            self.remain.set(f"Remain: {remain}")
            for movie in self.list_movie:
                if self.index.get() == self.list_movie.index(movie):
                    movie[2] = movie[2] - int(self.seat.get())
            self.list_booking.append(
                [self.client_name.get(), self.selected.get(), int(self.seat.get()), movie[2],
                 movie[2] - int(self.seat.get())])
            self.seat.set(0)
        else:
            messagebox.showwarning(title="Unsuccess", message=f"Your seat is invalid")

    def print_booking(self, e):
        temp = "\n".join(
            [f"{i+1}.{info[0]} : {info[1]} seats/Remaining : {info[2]}" for i, info in enumerate(self.list_movie)])
        messagebox.showinfo("Booking Summary", temp)

    def print_report(self, e):
        name = self.selected.get()
        index = self.movie_show.index(name)
        card_type = self.card_type.get()
        for movie in self.list_movie:
            if index == self.list_movie.index(movie):
                name_movie = movie[0]
                seats = movie[1]
                price = movie[3]
        number_of_movie = 1
        now_seat = 0
        for info in self.list_booking:
            if info[1] == name_movie:
                now_seat = now_seat + info[2]
        if card_type == "S":
            discount = price * 0.05
        elif card_type == "B":
            discount = price * 0.10
        elif card_type == "G":
            discount = price * 0.15
        else:
            discount = 0
        list_report = []
        for info in self.list_booking:
            if info[1] == name_movie:
                list_report.append(f"{number_of_movie}.{info[0]} {info[2]} seats, Total Price: "
                                   f"{((price*info[2])-(discount*info[2])):.0f} bath. "
                                   f"(Discount: {discount*info[2]:.0f} bath)")
                number_of_movie = number_of_movie + 1
        temp = "\n".join(list_report)
        total = f"   Total {now_seat} seats"
        messagebox.showinfo(title="Report", message=temp + "\n" + total)

    def select(self, e):
        name = self.selected.get()
        index = self.movie_show.index(name)
        remain = self.list_movie[index][2]
        Price = self.list_movie[index][3]
        self.index.set(index)
        self.remain.set(f"Remain: {remain}, Price: {Price}")

    def guess(self, e):
        messagebox.showinfo(title="Login Success", message=f"Hello, {self.client_name.get()}")
        self.client_name2.set("Welcome: " + self.client_name.get())
        self.window9.withdraw()
        self.winlogindown()
        self.winfirstdown()
        self.window5.deiconify()

    def __init__(self, window1):
        # 1 First Window
        self.client_name = StringVar()
        self.client_name2 = StringVar()
        self.gender2 = StringVar()
        self.card_type = StringVar()
        self.window1 = window1
        self.window1.geometry("300x350")
        self.window1.title("Theater")
        self.list_movie = []
        self.movie_show = []
        self.list_booking = []
        welcome_logo = PhotoImage(file=f"Welcome_logo.png")
        Label(self.window1, image=welcome_logo).pack()
        ### Account Button
        account_logo = PhotoImage(file=f"Account_logo.png")
        account_button = Button(self.window1, text="ID", image=account_logo, compound=LEFT, padx=5)
        account_button.bind("<Button-1>", self.winloginup)
        account_button.pack(padx=5, pady=1)
        # Guest Button
        guest_logo = PhotoImage(file=f"Guest_logo2.png")
        guest_button = Button(self.window1, text="Guest", image=guest_logo, compound=LEFT, padx=5)
        guest_button.bind("<Button-1>", self.win9up)
        guest_button.pack(padx=5, pady=5)
        # 9 Window ID
        self.window9 = Toplevel()
        self.window9.title("Login")
        self.ID = StringVar()
        ## ID_number Picture
        guest_login_logo = PhotoImage(file=f"Guest_login_logo.png")
        Button(self.window9, text="Name:", image=guest_login_logo, compound=LEFT, padx=1, bd=0).pack(side=LEFT, padx=1,
                                                                                                     pady=5)
        Entry(self.window9, textvariable=self.client_name, width=10, justify=RIGHT).pack(side=LEFT, padx=5)
        ## Login Button
        loginG_logo = PhotoImage(file="Login_logo.png")
        loginG_button = Button(self.window9, image=loginG_logo, compound=LEFT, text="Log in", bd=0)
        loginG_button.bind("<Button-1>", self.guess)
        loginG_button.pack(padx=5)
        ## Back to first window Button
        back9_logo = PhotoImage(file=f"Back_logo.png")
        back8_button = Button(self.window9, text="Back", image=back9_logo, compound=LEFT, padx=5, bd=0)
        back8_button.bind("<Button-1>", self.win9down)
        back8_button.pack(side=BOTTOM)
        self.window9.withdraw()
        # 3 Window ID
        self.window3 = Toplevel()
        self.window3.title("Login")
        self.ID = StringVar()
        ## ID_number Picture
        ID_logo = PhotoImage(file=f"ID_logo.png")
        Button(self.window3, text="ID:", image=ID_logo, compound=LEFT, padx=5, bd=0).pack(side=LEFT, padx=5, pady=5)
        Entry(self.window3, textvariable=self.ID, width=10, justify=RIGHT).pack(side=LEFT, padx=5)
        ## Login Button
        login_logo = PhotoImage(file="Login_logo.png")
        login_button = Button(self.window3, image=login_logo, compound=LEFT, text="Log in", bd=0)
        login_button.bind("<Button-1>", self.click)
        login_button.pack(padx=5)
        ## Back to first window Button
        back4_logo = PhotoImage(file=f"Back_logo.png")
        back4_button = Button(self.window3, text="Back", image=back4_logo, compound=LEFT, padx=5, bd=0)
        back4_button.bind("<Button-1>", self.winlogindown2)
        back4_button.pack(side=BOTTOM)
        self.gender = StringVar()
        self.window3.withdraw()
        # 5 Window Movie
        self.window5 = Toplevel()
        self.window5.option_add("*Font", "consola 10")
        self.window5.title("Theater Menu")
        self.window5.geometry("300x300")
        ## People Logo
        person_logo = PhotoImage(file="Person_logo.png")
        person_button = Label(self.window5, image=person_logo, compound=LEFT, textvariable=self.client_name2,
                              bd=0, padx=5, pady=5)
        person_button.config(font=("Courier", 15))
        person_button.pack()
        ### Movie Button
        movie_logo = PhotoImage(file="Movie_logo.png")
        movie_button = Button(self.window5, image=movie_logo, compound=LEFT, text="Movie", padx=4.5)
        movie_button.bind("<Button-1>", self.win6up)
        movie_button.pack(pady=5)
        # 6 Window Movie Show
        self.window6 = Toplevel()
        self.window6.title("Movie's list")
        list_logo2 = PhotoImage(file="List_logo2.png")
        list_logo = Label(self.window6, image=list_logo2, compound=LEFT, text="List of Movie", padx=4.5)
        list_logo.config(font=("Courier", 20))
        list_logo.pack(pady=5)
        self.add_movie_and_capacity()
        self.add_movie_for_show()
        movie_show_logo = PhotoImage(file="Movie_show_logo.png")
        for info in self.list_movie:
            btn = Label(self.window6, image=movie_show_logo, text=info[0] + " : " + str(info[1]) + " seats",
                        compound=LEFT, borderwidth=0, padx=10)
            btn.config(font=("Courier", 15))
            btn.pack(padx=20,anchor=W)
            btn.bind("<Button-1>", self.on_click)
        ## Back to Movie
        back5_logo = PhotoImage(file=f"Back_logo.png")
        back5_button = Button(self.window6, text="Back", image=back5_logo, compound=LEFT, padx=5, bd=0)
        back5_button.bind("<Button-1>", self.win6down)
        back5_button.pack(side=RIGHT)
        self.window6.withdraw()
        ### Reservation Button
        reservation_logo = PhotoImage(file="Reservation_logo.png")
        reservation_button = Button(self.window5, image=reservation_logo, compound=LEFT, text="Booking")
        reservation_button.bind("<Button-1>", self.win7up)
        reservation_button.pack(pady=5)
        self.window7 = Toplevel()
        self.window7.title("Reservation")
        self.window7.geometry("250x310")
        reserve_logo = PhotoImage(file="Reserve_logo.png")
        Label(self.window7, image=reserve_logo, compound=LEFT, text="Booking", padx=5).pack(pady=5)
        self.selected = StringVar()
        self.remain = StringVar()
        self.index = IntVar()
        self.selected.set(self.movie_show[0])
        self.remain.set(f"Remain: {self.list_movie[0][2]}, Price: {self.list_movie[0][3]}")
        Label(self.window7, textvariable=self.remain, width=20).pack()
        btn = OptionMenu(self.window7, self.selected, *self.movie_show, command=self.select)
        btn.config(width=20)
        btn.pack(padx=20)
        seat_logo = PhotoImage(file="seat_logo.png")
        Label(self.window7, image=seat_logo).pack()
        self.seat = IntVar()
        Entry(self.window7, textvariable=self.seat, width=5, justify=CENTER).pack()
        ## Submit Button
        submit2_logo = PhotoImage(file=f"Submit_logo.png")
        submit2_button = Button(self.window7, image=submit2_logo, compound=LEFT, text="Submit", padx=5, bd=0)
        submit2_button.bind("<Button-1>", self.booking)
        submit2_button.pack(padx=5, pady=5)
        ## Summary Button
        summary_logo = PhotoImage(file=f"Summary_logo6.png")
        summary_button = Button(self.window7, text="Summary", image=summary_logo, compound=TOP, padx=5, bd=0)
        summary_button.bind("<Button-1>", self.print_booking)
        summary_button.pack(side=LEFT, padx=7)
        report3_logo = PhotoImage(file="Report_logo.png")
        report3_button = Button(self.window7, image=report3_logo, compound=TOP, text="Report", padx=4, bd=0)
        report3_button.bind("<Button-1>", self.win7downandwin8up)
        report3_button.pack(side=LEFT, padx=10)
        ## Back to Movie
        back7_logo = PhotoImage(file=f"Back_logo.png")
        back7_button = Button(self.window7, text="Back", image=back7_logo, compound=LEFT, padx=5, bd=0)
        back7_button.bind("<Button-1>", self.win7down)
        back7_button.pack(side=LEFT, padx=10)
        self.window7.withdraw()
        ### Report Button
        report_logo = PhotoImage(file="Report_logo.png")
        report_button = Button(self.window5, image=report_logo, compound=LEFT, text="Report", padx=4)
        report_button.bind("<Button-1>", self.win8up)
        report_button.pack(pady=5)
        self.window8 = Toplevel()
        self.window8.title("Report")
        self.window8.geometry("220x200")
        report2_logo = PhotoImage(file="Report_logo2.png")
        Label(self.window8, image=report2_logo, compound=LEFT, text="Report", padx=4).pack(pady=5)
        btn2 = OptionMenu(self.window8, self.selected, *self.movie_show, command=self.select)
        btn2.config(width=20)
        btn2.pack(padx=30, pady=5)
        ## Searching Button
        reporting_logo = PhotoImage(file=f"Search_logo.png")
        reporting_button = Button(self.window8, text="Check", image=reporting_logo, compound=LEFT, padx=5, bd=0)
        reporting_button.bind("<Button-1>", self.print_report)
        reporting_button.pack(pady=3)
        ## Back to Movie
        back8_logo = PhotoImage(file=f"Back_logo.png")
        back8_button = Button(self.window8, text="Back", image=back8_logo, compound=LEFT, padx=5, bd=0)
        back8_button.bind("<Button-1>", self.win8down)
        back8_button.pack(side=RIGHT, pady=3)
        ## Back to Booking
        back_booking_button = Button(self.window8, text="Booking", image=reservation_logo, compound=LEFT, padx=5, bd=0)
        back_booking_button.bind("<Button-1>", self.win8downandwin7up)
        back_booking_button.pack(side=LEFT)
        self.window8.withdraw()
        ## Back to first window Button
        back3_logo = PhotoImage(file=f"Back_logo.png")
        back3_button = Button(self.window5, text="Back", image=back3_logo, compound=LEFT, padx=5, bd=0)
        back3_button.bind("<Button-1>", self.back_to_first)
        back3_button.pack(side=LEFT)
        ### Exit Button
        exit1_logo = PhotoImage(file=f"Exit_logo.png")
        exit1_button = Button(self.window5, text="Exit", image=exit1_logo, compound=LEFT, bd=0)
        exit1_button.bind("<Button-1>", self.Exit)
        exit1_button.pack(side=RIGHT, padx=5)
        self.window5.withdraw()
        ### Register Button
        register_logo = PhotoImage(file=f"Register_logo.png")
        register_button = Button(self.window1, text="Register", image=register_logo, compound=LEFT, padx=5)
        register_button.bind("<Button-1>", self.winregisterup)
        register_button.pack(padx=5)
        # 4 Window Registration
        self.window4 = Toplevel()
        self.window4.title("Register")
        regis_logo = PhotoImage(file=f"Registration_logo.png")
        Button(self.window4, text="Registration", image=regis_logo, compound=LEFT, padx=1, pady=5, bd=0).pack(padx=50)
        Label(self.window4, text="Name").pack()
        Entry(self.window4, textvariable=self.client_name, width=20, justify=CENTER).pack(padx=5, pady=5)
        Label(self.window4, text="Gender[Male/Female]").pack()
        Entry(self.window4, textvariable=self.gender, width=10, justify=CENTER).pack(padx=5, pady=5)
        Label(self.window4, text="Card type[(S)ilver, (B)lue , (G)old]").pack()
        Entry(self.window4, textvariable=self.card_type, width=10, justify=CENTER).pack(padx=5, pady=5)
        ## Back to first window Button
        back2_logo = PhotoImage(file=f"Back2_logo.png")
        back_button = Button(self.window4, text="Back", image=back2_logo, compound=LEFT, padx=5, bd=0)
        back_button.bind("<Button-1>", self.winregisdown2)
        back_button.pack(side=LEFT)
        ## Submit Button
        submit_logo = PhotoImage(file=f"Submit_logo.png")
        submit_button = Button(self.window4, image=submit_logo, compound=LEFT, text="Submit", padx=5, bd=0)
        submit_button.bind("<Button-1>", self.register)
        submit_button.pack(side=RIGHT, padx=5, pady=5)
        self.window4.withdraw()
        ### Rate Button
        rate_logo = PhotoImage(file=f"Rate_logo.png")
        rate_button = Button(self.window1, text="Rating", image=rate_logo, compound=LEFT, padx=5, bd=0)
        rate_button.bind("<Button-1>", self.winrateup)
        rate_button.pack(side=LEFT, padx=5, pady=5)
        ### Exit Button
        exit_logo = PhotoImage(file=f"Exit_logo.png")
        exit_button = Button(self.window1, text="Exit", image=exit_logo, compound=LEFT, padx=5, bd=0)
        exit_button.bind("<Button-1>", self.Exit)
        exit_button.pack(side=RIGHT, padx=5, pady=5)
        # 2 Window Rating
        self.window2 = Toplevel()
        self.window2.title("Rating")
        feelings = ['vd', 'd', 'n', 's', 'vs']
        feelings_text = ['a', 'b', 'c', 'd', 'e']
        images = [f'{s}.png' for s in feelings]
        photos = [PhotoImage(file=img) for img in images]
        Button(self.window2, image=photos[1], text=feelings[1], borderwidth=0)
        ## See result to first window Button
        result_logo = PhotoImage(file=f"Result_logo.png")
        result_button = Button(self.window2, text="Result", image=result_logo, compound=LEFT, padx=5, bd=0)
        result_button.bind("<Button-1>", self.rating_result)
        result_button.pack(side=LEFT, padx=5, pady=5)
        for i in range(len(images)):
            btn = Button(self.window2, image=photos[i], text=feelings_text[i], borderwidth=0, padx=20)
            btn.pack(side=LEFT)
            btn.bind("<Button-1>", self.on_click)
        ## Back to first window Button
        back_logo = PhotoImage(file=f"Back_logo.png")
        back_button = Button(self.window2, text="Back", image=back_logo, compound=LEFT, padx=5, bd=0)
        back_button.bind("<Button-1>", self.winratedown)
        back_button.pack(side=RIGHT, padx=5, pady=5)
        self.window2.withdraw()
        window1.mainloop()


window = Tk()
sample = first_page(window)
print("All done!")
