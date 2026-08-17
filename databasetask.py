import sqlite3
import sys
import subprocess
import time

def createtables(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS "Customers" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "Name"	TEXT NOT NULL,
        "Surname"	TEXT NOT NULL,
        "Email"	TEXT NOT NULL,
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

def wipedatabase(cur, tablelist):
    for i in tablelist:
        cur.execute(f"""DROP TABLE IF EXISTS "{i}";""")

def addsampledata(cur):
    print('adding sample data')
    cur.execute("""INSERT INTO "Customers" (Name, Surname, Email, PhoneNumber, Password)
VALUES ('Jacob', 'Hewitt', 'jacobhart@hotmail.com', '0492464541', 'dingdong17'),
('Paul', 'Holmes', 'hackerman@yahoo.com', '0444221222', 'paulsgardenaccount'),
('Luke', 'Antonelli', 'lukeyboysemail@gmail.com', '04942987', 'L1R1B1'),
('Jayden', 'Yap', 'jaydenspersonalemail@outlook.com', '0428371811', 'sillybilly'),
('Jon', 'Iodine', 'iodinesman@gmail.com', '0411911931', 'chemicalsareneat'),
('Donald', 'Trump', 'donaldjtrump@gmail.com', '08942931', 'bombiranortheyllexpand');""")

    cur.execute("""INSERT INTO Bookings (CustomerID, DateOfWork, DateOrdered, WorkComplete, PaymentMethod, HasPaid, Address)
VALUES (1, "2026-08-19", "2026-07-24", 1, "Credit Card", 0, "1 Lenina Avenue"),
(3, "2026-08-17", "2026-08-02", 1, "Credit Card", 0, "7 Revesby Road"),
(4, "2026-08-11", "2026-07-15", 1, "Cash", 1, "392 Huntriss Road"),
(5, "2026-09-07", "2026-08-19", 0, "Cash", 0, "85 Nicholson Road");""")

    cur.execute("""INSERT INTO "Services" (Name, Cost, Hours)
VALUES ('Lawn Mowing', 60, 1), 
('Edging', 40, 0.5),
('Fertilising', 60, 1),
('Weed Removal', 60, 1),
('Garden Clean-Up', 50, 0.75);""")

    cur.execute("""INSERT INTO "Services-Bookings" (BookingID, ServiceID)
VALUES (1, 1), (1, 2), (2, 1), (3, 1), (3, 3), (4, 1), (4, 4);""")

    cur.execute("""INSERT INTO Mowers (Name, Surname, Email, Password, Owner)
VALUES ("Nick", "Lee", "nick.lee-work@gmail.com", "nickspassword", 1),
("Lucas", "Aitkins", "l-a-owner-lawncare@outlook.com", "alfaralto123", 1),
("Jenna", "Benson", "jennasowneremail@gmail.com", "jennaskey1!", 1),
("Matthew", "Champneys", "matthewtheworker@outlook.com", "mattsbigboyaccount", 0),
("Ben", "Dover", "bendover@outlook.com", "gardening@52years", 0);""")

    cur.execute("""INSERT INTO Jobs (MowerID, ServiceBookingID, HoursWorked, AmountOwed)
VALUES (1, 1, 1, 40), (1, 2, 0.5, 25), (2, 3, 0.5, 25), (1, 3, 0.5, 25), (3, 4, 1, 40), (4, 5, 1, 40), (1, 6, 0, 0);""")

def validateinput(question, validinputs, errormessage):
    while True:
        userinput = input(question)
        if userinput in validinputs:
            return userinput
        elif userinput == "exit":
            sys.exit()
        else:
            print(errormessage)

def clear_screen():
    # Use 'cls' for Windows, 'clear' for Linux/macOS
    command = 'cls' if sys.platform == 'win32' else 'clear'
    subprocess.run(command, shell=True)

def customerinterface():
    time.sleep(0.5)
    clear_screen()
    loginchoice = validateinput("Do you want to log in to an existing account or create a new account? (log in or create account) ", ["log in", "create account"], "Please input one of the options: log in or create account")
    if loginchoice == "log in":
        login()
    elif loginchoice == "create account":
        createaccount()

def createaccount():
    print("creating account")

def login():
    print("logging in")
    cur.execute("SELECT Email FROM Customers")
    emails = [row[0] for row in cur.fetchall()]
    useremail = validateinput("WHat is the email associated with your account? ", emails, "Please input an email associated with an account.")

def employeeinterface():
    print('employee')

def ownerinterface():
    print('owner')
           
con = sqlite3.connect("greenerdayslawncare.db") #connects or creates the database file
cur = con.cursor() #This is necessary to allow us to use SQL queries
createtables(cur) #will create the tables if they don't exist

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