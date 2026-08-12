INSERT INTO Customers (Name, Surname, Email, PhoneNumber, Password)
VALUES ("Jacob", "Hewitt", "jacobhart@hotmail.com", "0492464541", "dingdong17"),
("Paul", "Holmes", "hackerman@yahoo.com", "0444221222", "paulsgardenaccount"),
("Luke", "Antonelli", "lukeyboysemail@gmail.com", "04942987", "L1R1B1"),
("Jayden", "Yap", "jaydenspersonalemail@outlook.com", "0428371811", "sillybilly"),
("Jon", "Iodine", "iodinesman@gmail.com", "0411911931", "chemicalsareneat"),
("Donald", "Trump", "donaldjtrump@gmail.com", "08942931", "bombiranortheyllexpand");

INSERT INTO Bookings (CustomerID, DateOfWork, DateOrdered, WorkComplete, PaymentMethod, HasPaid, Address)
VALUES (1, "2026-08-19", "2026-07-24", 1, "Credit Card", 0, "1 Lenina Avenue"),
(3, "2026-08-17", "2026-08-02", 1, "Credit Card", 0, "7 Revesby Road"),
(4, "2026-08-11", "2026-07-15", 1, "Cash", 1, "392 Huntriss Road"),
(5, "2026-08-29", "2026-08-19", 0, "Cash", 0, "85 Nicholson Road");

INSERT INTO Services (Name, Cost, Hours)
VALUES ("Lawn Mowing", 60, 1), 
("Edging", 40, 0.5),
("Fertilising", 60, 1),
("Weed Removal", 60, 1),
("Garden Clean-Up", 50, 0.75);

INSERT INTO "Services-Bookings" (BookingID, ServiceID)
VALUES (1, 1), (1, 2), (2, 1), (3, 1), (3, 3), (4, 1), (4, 4);

INSERT INTO Mowers (Name, Surname, Email, Password, Owner)
VALUES ("Nick", "Lee", "nick.lee-work@gmail.com", "nickspassword", 1),
("Lucas", "Aitkins", "l-a-owner-lawncare@outlook.com", "alfaralto123", 1),
("Jenna", "Benson", "jennasowneremail@gmail.com", "jennaskey1!", 1),
("Matthew", "Champneys", "matthewtheworker@outlook.com", "mattsbigboyaccount", 0)
("Ben", "Dover", "bendover@outlook.com", "gardening@52years", 0);

INSERT INTO Jobs (MowerID, ServiceBookingID, HoursWorked, AmountOwed)
VALUES (1, 1, 1, 40), (1, 2, 0.5, 25), (2, 3, 0.5, 25), (1, 3, 0.5, 25), (3, 4, 1, 40), (4, 5, 1, 40), (1, 6, 0, 0);