SELECT CustomerID, DateOfWork, PaymentMethod, HasPaid
FROM "Bookings"
WHERE DateOfWork < CURRENT_DATE;
-- a simple query that shows past bookings from a customer

SELECT Services.Name, Services.Hours, Bookings.DateOfWork, Bookings.Address
FROM "Mowers"
JOIN Jobs ON Jobs.MowerID = Mowers.ID
JOIN "Services-Bookings" ON "Services-Bookings".ID = Jobs.ServiceBookingID
JOIN Services ON Services.ID = "Services-Bookings".ServiceID
JOIN Bookings ON Bookings.ID = "Services-Bookings".BookingID
WHERE DateOfWork > CURRENT_DATE AND Mowers.Name == "Nick";
-- this query will find all of the service names, hours required, dates and addresses for Nick's jobs

UPDATE Jobs
SET MowerID = 4
WHERE ServiceBookingID IN (
    SELECT ID
    FROM "Services-Bookings"
    JOIN "Bookings" ON Bookings.ID = "Services-Bookings".BookingID
    WHERE Bookings.CustomerID == 3;
);
-- this query will change the mower assigned to all jobs of a specific customer, for example if they request a specific mower
-- the subquery is necessary to join together tables in SQLite syntax

DELETE FROM Mowers
WHERE ID IN (
	SELECT Jobs.MowerID
	FROM Jobs
	JOIN "Services-Bookings" ON "Services-Bookings".ID = Jobs.ServiceBookingID
	JOIN Bookings ON Bookings.ID = "Services-Bookings".BookingID
	WHERE Bookings.DateOfWork > date('now', '-365 days')
	GROUP BY Jobs.MowerID
	HAVING SUM(Jobs.HoursWorked) = 0)
OR ID NOT IN (
	SELECT Jobs.MowerID
	FROM Jobs
	JOIN "Services-Bookings" ON "Services-Bookings".ID = Jobs.ServiceBookingID
	JOIN Bookings ON Bookings.ID = "Services-Bookings".BookingID
	WHERE Bookings.DateOfWork > date('now', '-365 days'))
--this query deletes workers that have either: not done a job, or not worked any hours for the last year
--this query could be useful if the company is hypothetically trying to lay off workers for productivity

