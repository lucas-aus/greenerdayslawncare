import sqlite3

def connecttodatabase():
    con = sqlite3.connect("greenerdayslawncare.db")
    cur = con.cursor() #This is necessary to allow us to use SQL queries
    return cur

def createtables(cur):
    cur.execute("""CREATE TABLE "Customers" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "Name"	TEXT NOT NULL,
        "Surname"	TEXT NOT NULL,
        "Email"	TEXT NOT NULL,
        "PhoneNumber"	TEXT,
        "Password"	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT));""")
    
    cur.execute("""CREATE TABLE "Bookings" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"CustomerID"	INTEGER NOT NULL,
	"DateOfWork"	TEXT NOT NULL,
	"DateOrdered"	TEXT NOT NULL,
	"PaymentMethod"	TEXT NOT NULL,
	"HasPaid"	INTEGER NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("CustomerID") REFERENCES "Customers"("ID"));""")

    cur.execute("""CREATE TABLE "Services" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "Name"	TEXT NOT NULL UNIQUE,
        "Cost"	INTEGER NOT NULL,
        "Hours"	INTEGER NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
    );""")

    cur.execute("""CREATE TABLE "Services-Bookings" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "ServiceID"	INTEGER NOT NULL,
        "BookingID"	INTEGER NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("BookingID") REFERENCES "Bookings"("ID"),
        FOREIGN KEY("ServiceID") REFERENCES "Services"("ID")
    );""")

    cur.execute("""CREATE TABLE "Jobs" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"MowerID"	INTEGER NOT NULL,
	"ServiceBookingID"	INTEGER NOT NULL,
	"HoursWorked"	INTEGER NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("MowerID") REFERENCES "Mowers"("ID"),
	FOREIGN KEY("ServiceBookingID") REFERENCES "Services-Bookings"("ID"));""")

def wipedatabase(cur, tablelist):
    for i in tablelist:
        cur.execute(f"DROP TABLE IF EXIST {i};")

def addsampledata(cur):
    

cur = connecttodatabase()
createtables(cur)