show databases;
create database edyoda_assignment;
use edyoda_assignment;
CREATE TABLE SalesPeople(Snum INT PRIMARY KEY,Sname VARCHAR(20) 
NOT NULL UNIQUE,City VARCHAR(20),Comm INT);

CREATE TABLE Customers(Cnum INT PRIMARY KEY,Cname VARCHAR(20),City varchar(20) 
NOT NULL,Snum INT,FOREIGN KEY(Snum) REFERENCES SalesPeople
(Snum) );

CREATE TABLE Orders(Onum INT PRIMARY KEY,Amt FLOAT(10,2),
Odate DATE,Cnum INT,Snum INT,FOREIGN KEY (Cnum) REFERENCES 
Customers(Cnum),FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);

INSERT INTO SalesPeople(Snum ,Sname ,City ,Comm) values (1001 ,"Peel" ,
"London" ,12),

(1002  ,"Serres", "Sanjose" ,13),

(1004 ,"Motika" ,"London" ,11),

(1007 ,"Rifkin", "Barcelona" ,15),

(1003 ,"Axelrod", "Newyork" ,10);


INSERT INTO Customers(Cnum ,Cname ,City ,Snum) VALUES 
(2001  ,"Hoffman" ,"London", 1001),

(2002  ,"Giovanni" ,"Rome" ,1003),

(2003  ,"Liu" ,"Sanjose" ,1002),

(2004  ,"Grass" ,"Berlin" ,1002),

(2006 ,"Clemens" ,"London" ,1001),

(2008 ,"Cisneros" ,"Sanjose" ,1007),

(2007 ,"Pereira" ,"Rome" ,1004);

select * from SalesPeople;
select * from Customers;
select * from Orders;

INSERT INTO Orders(Onum ,Amt ,Odate ,Cnum ,Snum) VALUES
(3001 ,18.69 ,"1990-10-03" ,2008 ,1007),

(3003 ,767.19 ,"1990-10-03" ,2001 ,1001),

(3002 ,1900.10 ,"1990-10-03" ,2007 ,1004),

(3005  ,5160.45, "1990-10-03", 2003, 1002),

(3006  ,1098.16, "1990-10-03", 2008, 1007),

(3009 ,1713.23, "1990-10-04", 2002, 1003),

(3007,  75.75, "1990-10-04", 2004, 1002),

(3008  ,4273.00, "1990-10-05", 2006, 1001),

(3010  ,1309.95, "1990-10-06", 2004, 1002),

(3011  ,9891.88, "1990-10-06", 2006, 1001);

SELECT count(*) FROM SalesPeople WHERE Sname LIKE 'A%' OR Sname LIKE 'a%';

SELECT DISTINCT SalesPeople.Snum,SalesPeople.Sname,SalesPeople.Comm,SalesPeople.City
FROM SalesPeople INNER JOIN Orders ON SalesPeople.Snum=Orders.Snum WHERE Orders.Amt>2000 ;

SELECT count(*) FROM SalesPeople WHERE City="Newyork";

SELECT count(*) FROM SalesPeople WHERE City="London" OR City="Paris";

SELECT count(*),Odate FROM Orders GROUP BY Odate ORDER BY count(*) ;





