SELECT CustomerID, Address, DateOfWork
FROM "Bookings"
WHERE DateOfWork > CURRENT_DATE;