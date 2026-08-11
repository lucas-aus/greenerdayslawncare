INSERT INTO Customers (Name, Surname, Email, PhoneNumber, Password)
VALUES ("Jacob", "Hart", "jacobhart@hotmail.com", "0492464541", "dingdong17"),
("Paul", "Hartwell", "hackerman@yahoo.com", "0444221222", "paulsgardenaccount"),
("Luke", "Avucurelli", "lukeyboysemail@gmail.com", "04942987", "L1R1B1"),
("Jayden", "Yap", "jaydenspersonalemail@outlook.com", "0428371811", "sillybilly"),
("Jon", "Iodine", "iodinesman@gmail.com", "0411911931", "chemicalsareneat"),
("Donald", "Trump", "donaldjtrump@gmail.com", "08942931", "bombiranortheyllexpand");

INSERT INTO Bookings (CustomerID, DateOfWork, DateOrdered, WorkComplete PaymentMethod, HasPaid)
VALUES (1, "22/08/2026", "24/07/2026", 1, "Credit Card", 0),
(3, "17/08/2026", "02/08/2026", 1, "Credit Card", 0),
(4, "11/08/2026", "15/07/2026", 1, "Cash", 1),
(5, "29/08/2026", "19/08/2026", 0, "Cash", 0);

INSERT INTO Services (Name, Cost, Hours)
VALUES ("Lawn Mowing", 60, 1), 
("Edging", 40, 0.5),
("Fertilising", 60, 1),
("Weed Removal", 60, 1),
("Garden Clean-Up", 50, 0.75);