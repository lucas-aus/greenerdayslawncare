import sqlite3
import sys
import subprocess
import time

def createtables(cur): #the SQL queries to create each table (if they don't exist) are enacted
    cur.execute("""CREATE TABLE IF NOT EXISTS "Customers" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "Name"	TEXT NOT NULL,
        "Surname"	TEXT NOT NULL,
        "Email"	TEXT NOT NULL UNIQUE,
        "PhoneNumber"	TEXT,
        "Password"	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS "Bookings" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"CustomerID"	INTEGER NOT NULL,
	"DateOfWork"	TEXT NOT NULL,
	"DateOrdered"	TEXT NOT NULL,
	"WorkComplete"	TEXT NOT NULL,
	"PaymentMethod"	TEXT NOT NULL,
	"HasPaid"	INTEGER NOT NULL,
	"Address"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("CustomerID") REFERENCES "Customers"("ID"));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "Services" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL UNIQUE,
	"Cost"	REAL NOT NULL,
	"Hours"	REAL NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "Services-Bookings" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "ServiceID"	INTEGER NOT NULL,
        "BookingID"	INTEGER NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("BookingID") REFERENCES "Bookings"("ID"),
        FOREIGN KEY("ServiceID") REFERENCES "Services"("ID"));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "Mowers" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL,
	"Surname"	TEXT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Password"	TEXT NOT NULL,
	"Owner"	INTEGER NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "Jobs" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"MowerID"	INTEGER NOT NULL,
	"ServiceBookingID"	INTEGER NOT NULL,
	"HoursWorked"	REAL NOT NULL,
    "AmountOwed"    REAL NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("MowerID") REFERENCES "Mowers"("ID"),
	FOREIGN KEY("ServiceBookingID") REFERENCES "Services-Bookings"("ID"));""")

def wipedatabase(cur, tablelist): #will remove all of the tables from the database
    for i in tablelist:
        cur.execute(f"""DROP TABLE IF EXISTS "{i}";""")

def addsampledata(cur): #adds all of the sample data if it doesnt exist yet
    cur.execute("""INSERT OR IGNORE INTO Customers (Name, Surname, Email, PhoneNumber, Password)
VALUES ("Jacob", "Hewitt", "jacobhewitt@hotmail.com", "0492464541", "dingdong17"),
("Paul", "Holmes", "hackerman@yahoo.com", "0444221222", "paulsgardenaccount"),
("Luke", "Antonelli", "lukeyboysemail@gmail.com", "04942987", "L1R1B1"),
("Jayden", "Yap", "jaydenspersonalemail@outlook.com", "0428371811", "sillybilly"),
("Jon", "Iodine", "iodinesman@gmail.com", "0411911931", "chemicalsareneat"),
("Donald", "Trump", "donaldjtrump@gmail.com", "08942931", "bombiranortheyllexpand");""")

    cur.execute("""INSERT OR IGNORE INTO Bookings (ID, CustomerID, DateOfWork, DateOrdered, WorkComplete, PaymentMethod, HasPaid, Address)
VALUES (1, 1, "2026-08-19", "2026-07-24", 1, "Credit Card", 0, "1 Lenina Avenue"),
(2, 3, "2026-08-17", "2026-08-02", 1, "Credit Card", 0, "7 Revesby Road"),
(3, 4, "2026-08-11", "2026-07-15", 1, "Cash", 1, "392 Huntriss Road"),
(4, 5, "2026-09-07", "2026-08-19", 0, "Cash", 0, "85 Nicholson Road");""")

    cur.execute("""INSERT OR IGNORE INTO "Services" (ID, Name, Cost, Hours)
VALUES (1, 'Lawn Mowing', 60, 1), 
(2, 'Edging', 40, 0.5),
(3, 'Fertilising', 60, 1),
(4, 'Weed Removal', 60, 1),
(5, 'Garden Clean-Up', 50, 0.75);""")

    cur.execute("""INSERT OR IGNORE INTO "Services-Bookings" (ID, BookingID, ServiceID)
VALUES (1, 1, 1), (2, 1, 2), (3, 2, 1), (4, 3, 1), (5, 3, 3), (6, 4, 1), (7, 4, 4);""")

    cur.execute("""INSERT OR IGNORE INTO Mowers (ID, Name, Surname, Email, Password, Owner)
VALUES (1, "Nick", "Lee", "nick.lee-work@gmail.com", "nickspassword", 1),
(2, "Lucas", "Aitkins", "l-a-owner-lawncare@outlook.com", "alfaralto123", 1),
(3, "Jenna", "Benson", "jennasowneremail@gmail.com", "jennaskey1!", 1),
(4, "Matthew", "Champneys", "matthewtheworker@outlook.com", "mattsbigboyaccount", 0),
(5, "Ben", "Dover", "bendover@outlook.com", "gardening@52years", 0);""")

    cur.execute("""INSERT OR IGNORE INTO Jobs (ID, MowerID, ServiceBookingID, HoursWorked, AmountOwed)
VALUES (1, 1, 1, 1, 40), (2, 1, 2, 0.5, 25), (3, 2, 3, 0.5, 25), (4, 1, 3, 0.5, 25), (5, 3, 4, 1, 40), (6, 4, 5, 1, 40), (7, 1, 6, 0, 0);""")

def validateinput(question, validinputs, errormessage):
    while True:
        userinput = input(question)
        if userinput in validinputs:
            return userinput
        elif userinput == "exit":
            sys.exit()
        else:
            print(errormessage)

def clearscreen():
    #ckears the screen, using 'cls' for windows computers and 'clear' for everything else (bc apparently thats what you're supposed to do)
    command = 'cls' if sys.platform == 'win32' else 'clear'
    subprocess.run(command, shell=True)

def customerinterface():
    time.sleep(0.5)
    clearscreen()
    loginchoice = validateinput("Do you want to log in to an existing account or create a new account? (log in or create account) ", ["log in", "create account"], "Please input one of the options: log in or create account")
    if loginchoice == "log in":
        email = login()
    elif loginchoice == "create account":
        createaccount()
    clearscreen()
    editoradd = validateinput("Would you like to edit a booking, add a booking, or change customer details? (edit booking, add booking, or change details)? ", ["edit booking", "add booking", "change details"], "Please enter either edit booking, add booking, or change details.")
    if editoradd == 'change details':
        changecustomerdetails(email)
    elif editoradd == 'add booking':
        addbooking(email)
    elif editoradd == 'edit booking':
        editbooking(email)

def changecustomerdetails(email):
    element = validateinput("What would you like to change about your account? (name, surname, email, phone number, or password) ", ['name', 'surname', 'email', 'phone number', 'password'], "Please choose one of: name, surname, email, phone number, or password")
    newvalue = input(f"What would you like to change your {element} to? ")
    if element == "phone number":
        element = "PhoneNumber"
    cur.execute(f"""UPDATE Customers SET "{element}" = '{newvalue}' WHERE Email = '{email}'; """)
    con.commit()
    customerinterface()

def editbooking(email):
    print("")
    cur.execute(f"""SELECT Bookings.DateOfWork FROM Bookings JOIN Customers ON Customers.ID = Bookings.CustomerID WHERE Customers.Email = "{email}";""")
    bookings = [row[0] for row in cur.fetchall()]
    cur.execute(f"""SELECT DISTINCT Bookings.CustomerID FROM Bookings JOIN Customers ON Customers.ID = Bookings.CustomerID WHERE Customers.Email = "{email}";""")
    id = str([row[0] for row in cur.fetchall()][0])
    date = validateinput("What date is the booking you would like to change set for? Enter in YYYY-MM-DD format ", bookings, "Please answer a date with a booking.")
    element = validateinput("Which element of your booking would you like to change? (date of work, payment method, or address) ", ["date of work", 'payment method', 'address'], "Please enter date of work, payment method, or address.")
    if element == "date of work":
        element = "DateOfWork"
    elif element == "payment method":
        element = "PaymentMethod"
    elif element == "address":
        element = "Address"
    newvalue = input("What would you like to change this element to? ")
    cur.execute(f"""UPDATE Bookings SET {element} = '{newvalue}' WHERE Bookings.CustomerID = {id};""")
    con.commit()
    customerinterface()

def addbooking(email):
    print("")
    print("Adding booking details")
    dateofwork = input("What date would you like the work to occur? Enter in format YYYY-MM-DD ")
    while len(dateofwork) != 10:
        print("Ensure you enter in format YYYY-MM-DD.")
        dateofwork = input("What date would you like the work to occur? ")
    paymentmethod = validateinput("How will you pay? (Credit Card or Cash) ", ["Credit Card", "Cash"], "Please enter either credit card or cash.")
    address = input("Please enter the address of the house you would like the work done at. ")
    cur.execute(f"""INSERT INTO Bookings (CustomerID, DateOfWork, DateOrdered, WorkComplete, PaymentMethod, HasPaid, Address)
    VALUES ((SELECT Customers.ID FROM Customers WHERE Email = "{email}"), "{dateofwork}", "date('now')", 0, "{paymentmethod}", 0, "{address}");""")
    con.commit()
    customerinterface()
        

def createaccount(): #simply asks for information for a Customer record, and then puts it into the database.
    print("creating account")
    name = input("What is your first name? ")
    while " " in name or len(name) > 20: #This is not in the validate input function because it has length and content requirements ratehr than being from a list
        print("Ensure there are no spaces, and the length is less than 20.")
        name = input("What is your first name? ")
    print("")
    surname = input("What is your surname? ")
    while " " in surname or len(surname) > 30:
        print("Ensure there are no spaces, and the length is less than 30.")
        surname = input("What is your surname? ")
    print("")
    email = input("What is the email? ")
    cur.execute("SELECT Email FROM Customers;")
    emails = [row[0] for row in cur.fetchall()]
    while " " in email or len(email) > 40 or email in emails:
        print("Ensure length is less than 40, there are no spaces, and the email is not already in use.")
        email = input("What is your email? ")
    print("")
    while True:
        phone = input("What is your phone number? ")
        try:
            int(phone) #tests to see if only numbers in phone number
            if len(phone) <= 10:
                break
        except:
            print("Phone number must only use numbers")
        print("Please input a valid phone number.")
    print("")
    password = input("What is the password you want associated with the account? ")
    while len(password) < 5 or len(password) > 15:
        print("Please input valid password.")
        password = input("What is the password you want associated with the account? ")
    clearscreen()
    print(f"""First Name: {name}
Surname: {surname}
Email: {email}
Phone Number: {phone}
Password: {password}""")
    print("")
    confirm = input("Are these details okay? ")
    while confirm not in ['yes', 'no', 'y', 'n', 'affirmative', 'negative', 'Yes', 'No', 'YES', 'NO']:
        confirm = input("Are these details okay? ")
    if confirm in ['yes', 'y', 'affirmative', 'Yes', 'YES']:
        cur.execute(f"INSERT INTO Customers (Name, Surname, Email, PhoneNumber, Password) VALUES ('{name}', '{surname}', '{email}', '{phone}', '{password}');")
        con.commit()
    customerinterface() #sends back to the beginning of customer interface, meaning that they can log in if they want.

def login():
    print("logging in")
    cur.execute("SELECT Email FROM Customers;")
    emails = [row[0] for row in cur.fetchall()]
    useremail = validateinput("What is the email associated with your account? ", emails, "Please input an email associated with an account.")
    cur.execute(f"""SELECT Password FROM Customers WHERE Email = "{useremail}";""") #finds the associated password
    password = cur.fetchone()[0]
    validateinput(f"What is the password associated with the account with {useremail}? ", password, "Incorrect. Please try again.")
    return useremail
    

def employeeinterface():
    clearscreen()
    cur.execute("SELECT Mowers.Email FROM Mowers")
    emaillist = [row[0] for row in cur.fetchall()]
    email = validateinput("What is your employee email? ", emaillist, "Please answer a valid employee email.")
    action = validateinput("Would you like to log hours or edit employee information? (log hours or edit info) ", ["log hours", "edit info"], "Please answer log hours or edit info.")
    if action == "log hours":
        loghours(email)
    elif action == "edit info":
        editinfo(email)

def loghours(email):
    cur.execute(f"""SELECT Bookings.DateOfWork, Jobs.ID FROM Jobs JOIN "Services-Bookings" AS sb ON sb.ID = Jobs.ServiceBookingID JOIN Bookings ON Bookings.ID = sb.BookingID JOIN Mowers ON Mowers.ID = Jobs.MowerID WHERE Mowers.Email == '{email}';""")
    jobs = cur.fetchall()
    datelist = [row[0] for row in jobs]
    date = validateinput("What date was the job on? ", datelist, "Please pick a valid date that work occurred.")
    hours = int(input("How many hours would you like to log?"))
    jobid = next(row[1] for row in jobs if row[0] == date)
    cur.execute(f"""UPDATE Jobs SET Jobs.HoursWorked = {hours} WHERE Jobs.ID = {jobid};""")
    con.commit()

def editinfo(email):
    element = validateinput("What element would you like to change? (name, surname, email, password) ", ["name", "surname", "email", "password"], "Please choose one of (name, surname, email, password)")
    newvalue = input("What would you like to change it to? ")
    cur.execute(f"""UPDATE Mowers SET "{element}" = '{newvalue}' WHERE Email = '{email}'""")
    con.commit()
    employeeinterface()

def ownerinterface():
    print('owner')
           
con = sqlite3.connect("greenerdayslawncare.db") #connects or creates the database file
cur = con.cursor() #This is necessary to allow us to use SQL queries
createtables(cur) #will create the tables if they don't exist
addsampledata(cur) #adds sample data only if it is not already there
con.commit()

usertype = validateinput("Are you a customer, mower, or an owner? ", ['customer', 'mower', 'owner'], "Please enter one of the following values: employee, owner, or mower")
if usertype == 'customer':
    customerinterface()
elif usertype == 'mower':
    employeeinterface()
elif usertype == 'owner':
    ownerinterface()

while True:
    con = sqlite3.connect("greenerdayslawncare.db")
    cur = con.cursor() #This is necessary to allow us to use SQL queries

    choice = input("What do you want to do? ")
    if choice == 'wipe':
        wipedatabase(cur, ["Jobs", "Services-Bookings", "Mowers", "Services", "Bookings", "Customers"])
    elif choice == 'sample data':
        addsampledata(cur)

    con.commit()
    cur.close()
    con.close()