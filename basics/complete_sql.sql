create table IT_department AS select name, salary from employees where department = 'IT';

select * from IT_department;

create temporary table high_paid (name varchar(100), salary int);

insert into high_paid select name, salary from employees where salary > 50000; 

select * from high_paid;

WITH high_paid_cte AS (select name, salary from employees where salary > 50000)

Create table cte_table select * from high_paid_cte;

alter table IT_department add column email varchar(100);

alter table IT_department drop column salary;

delete from IT_department where name = 'Bob';

update IT_department SET email = 'testing@email.com', name='Bob' where name = 'David';

create table rides(
ride_id INT,
driver_id INT,
rider_id INT,
pickup_loc varchar(200),
drop_loc varchar(200),
ride_date timestamp,
primary key(ride_id, rider_id)
)

select * from rides;

insert into rides(ride_id, rider_id, pickup_loc) values (1, 100, 'Bangalore');
insert into rides(ride_id, rider_id, pickup_loc) values (1, 101, 'Bangalore');

alter table rides alter column pickup_loc set NOT NULL;
alter table rides add constraint driver_unique unique (driver_id);

insert into rides(ride_id, driver_id, rider_id, pickup_loc) values (1, NULL, 103, 'Bangalore');
insert into rides(ride_id, driver_id, rider_id, pickup_loc) values (2, 30, 103, 'Bangalore');  -- since 2nd primary key has different value, this composite key works without duplicate entry problem while inserting

insert into rides(ride_id, driver_id, rider_id, pickup_loc) values (3, 30, 103, 'Bangalore');  -- this wont work as 30 is unique key, which dont allow duplicates, but allows NULL values unlike primary key, while we can change one primary key and use it as a composite primary key, but unique key doesnt work that way.
insert into rides(ride_id, driver_id, rider_id, pickup_loc) values (3, NULL, 103, 'Bangalore');  -- this will work, as NULL values can be used instead of duplicate values.

create table ola_driver(driver_id int PRIMARY KEY, driver_name varchar(100), license INT);
create table ola_rides(ride_id int, rider_id int, driver_id int , pickup_loc varchar(200), fare numeric(10, 2), foreign key (driver_id) references ola_driver(driver_id));

select * from ola_rides;

INSERT INTO ola_driver(driver_id, driver_name, license) VALUES
(1, 'Ravi Kumar', 123456),
(2, 'Sita Sharma', 234567),
(3, 'Arjun Das', 345678),
(4, 'Priya Singh', 456789);

INSERT INTO ola_rides(ride_id, rider_id, driver_id, pickup_loc, fare) VALUES
(101, 1001, 1, 'MG Road, Bangalore', 250.50),
(102, 1002, 2, 'Koramangala, Bangalore', 320.00),
(103, 1003, 3, 'Whitefield, Bangalore', 410.75),
(104, 1004, 1, 'Jayanagar, Bangalore', 180.25),
(105, 1005, 4, 'Indiranagar, Bangalore', 290.00),
(106, 1006, 2, 'HSR Layout, Bangalore', 360.50);

delete from ola_driver where driver_id = 1; -- violates foreign key as you cant delete something which is linked with foreign key in another table, delete the row in that table first.
delete from ola_rides where driver_id = 1;

delete from ola_driver where driver_id = 1;

select * from ola_driver;  -- now got deleted succesfully, alternate method set CASCADE DELETE property so that when a row gets deleted in primary key table, the linked foreign key table rows also get deleted.

alter table ola_rides add column is_delete boolean default false;
select * from ola_rides;

-- incase we need to delete something, instead of hard deleting, we do soft delete, i.e. just flag the variable.

update ola_rides set is_delete = true where driver_id = 2;
select * from ola_rides; -- now the values are set to true/1. So that while data analysis - we can filter out the rows with is_delete = true, such that these values are not included and also not deleted.

create table ride_costs(ride_id int primary key, country varchar(100) default 'india', amount numeric(10, 2) check (amount>0));
select * from ride_costs;

insert into ride_costs values (1, 'usa', 100);
insert into ride_costs values (2, 200); -- mention columns to insert at specific rows
insert into ride_costs values (3, 'germany');

select * from ride_costs; 
insert into ride_costs (ride_id, country, amount) values (5,default,200);
insert into ride_costs (ride_id, country, amount) values (6,default,-200); -- violates check constraint, so wont run!

SELECT CASE  
	when 8 > 10 then 'true'
	else 'false'
end as test1

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    phone_number VARCHAR(15),
    total_spending NUMERIC(10, 2)
);

INSERT INTO customers (customer_id, customer_name, phone_number, total_spending) VALUES
(1, 'Gowtham', '9876543210', 1500.50),
(2, 'Anita', NULL, 2500.00),
(3, 'Rahul', '9123456780', NULL),
(4, 'Priya', NULL, NULL),
(5, 'Suresh', '9988776655', 3200.75),
(6, 'Meena', '9012345678', 0),
(7, 'Karthik', NULL, 450.25);

alter table customers alter column customer_name set not null;

select 
	case
		when phone_number is NULL then customer_name
	end as customers_no_num
from customers;

select  customer_name, 
	case
		when total_spending >  1000 then 'high spend'
		else 'low spend'
	end as high_spend
from customers;

select count(*) as no_phone from customers where phone_number is null;
select count(*) as no_phone from customers where phone_number is not null;

select customer_id, customer_name from customers where  phone_number is NULL or total_spending is NULL;

select customer_id, customer_name from customers where  phone_number is NULL and total_spending is NULL;

select customer_name, COALESCE(phone_number, 'not available') from customers;

select customer_name, coalesce(phone_number, '100') from customers;

select customer_name, coalesce(phone_number, NULL, '100') from customers; -- replaces null values with defined values.

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50),
    address VARCHAR(200)
);

INSERT INTO employee (emp_id, emp_name, email, department, address) VALUES
(1, 'Gowtham Madhevasamy', 'gowtham.m@example.com', 'IT', '123, MG Road, Bangalore'),
(2, 'Anita Sharma', 'anita.sharma@example.com', 'HR', '45, Park Street, Kolkata'),
(3, 'Rahul Verma', 'rahul.verma@example.com', 'Finance', '67, Brigade Road, Bangalore'),
(4, 'Priya Nair', NULL, 'Marketing', '89, MG Road, Mumbai'),
(5, 'Suresh Kumar', 'suresh.kumar@example.com', 'IT', '12, Residency Road, Bangalore'),
(6, 'Meena Iyer', 'meena.iyer@example.com', 'Finance', NULL),
(7, 'Karthik R', 'karthik.r@example.com', 'HR', '78, Park Street, Chennai'),
(8, 'Rohit Singh', 'rohit.singh@example.com', 'Marketing', '101, MG Road, Delhi'),
(9, 'Sneha Rao', 'sneha.rao@example.com', 'IT', '11, Brigade Road, Bangalore'),
(10, 'Vikram Patil', NULL, 'Finance', '55, Residency Road, Pune');

select length(emp_name) from employee;

select emp_name,
case
	when length(emp_name) > 10 then 'too long'
	when length(emp_name) between 5 and 10 then 'too short'
	else 'normal'
end as check_length
from employee;

select upper(emp_name) from employee;

select concat(emp_name, ' - ', department) from employee;

insert into employee values (11, ' Vikram   ', NULL, 'Finance', ' 55, Residency Road, Pune');

select trim(emp_name), length(trim(emp_name)) from employee;	

select replace(emp_name, ' ', '_') from employee;

select lower(replace(emp_name, ' ', '_')) from employee;

select lpad(emp_name, 25, '-') from employee;

select format(100000, 2) from employee;

-- Create the Customers table to store customer information
CREATE TABLE Customers1 (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL
);

-- Create the Orders table to store order details
CREATE TABLE Orders1 (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount INT,
	foreign key (customer_id) references Customers(customer_id)
	);

-- Insert data into the Customers table
INSERT INTO Customers1 (customer_id, customer_name) VALUES
(101, 'Alice'),
(102, 'Bob'),
(103, 'Charlie');

-- Insert data into the Orders table
INSERT INTO Orders1 (order_id, customer_id, order_amount) VALUES
(1, 101, 8000),   -- Alice has an order > 5000
(2, 101, 4500),   -- Alice has another order < 5000
(3, 102, 3000),   -- Bob's only order is < 5000
(4, 103, 9500),   -- Charlie has an order > 5000
(5, 103, 6000);   -- Charlie has a second order > 5000

select customer_name from customers1 where customer_id in (select customer_id from Orders1 where order_amount >= 5000);

-- exists : if the condition is met, then returns all rows orelse returns nothing.
-- we are checking customers table based on orders of orders table with amt > 5000, if there is a single value which matches 5000, then its true and thus all the values from CUSTOMERS TABLE gets displayed.

select * from customers1 where exists (select 1 from orders1 where order_amount > 5000);

-- this command fails so there is no output
select * from customers1 where exists (select 1 from orders1 where order_amount > 10000);

-- in vs exists difference : in checks regardless of finding a correct value till the end of the table. exists returns as soon as it found the matching condition.

select customer_name, (select sum(order_amount) from orders1 o where c.customer_id = o.customer_id) as total_spend from customers1 c;

-- using subquery like a derived table, giving an alias is good practice to a derived table.
select cus_name FROM (select length(customer_name) as cus_name from customers1) as TEMP_TABLE;

select customer_name, 
case
	when (select sum(order_amount) as order_value from orders1 where orders1.customer_id = customers1.customer_id) > (select avg(order_amount) as avg_order_amt from orders1) THEN 'more than avg amt'
	else 'below avg'
end as order_spend_type
from customers1;

-- Creating views + using subquery as a derived column for getting order amount (like a join command for users so the spending gets combined)

create view highvalue_customers as (select customer_name, (select sum(order_amount) from orders1 where orders1.customer_id = customers1.customer_id) as total_spend from customers1); 

select * from highvalue_customers;

insert into orders1 values (6, 101, 10000);

select * from highvalue_customers; -- the view gets automatically updated as internally it runs the select query, so it gives the updated table + an abstraction to complex query + restricting certain columns

CREATE TABLE Employees_2 (
    EmployeeID INT PRIMARY KEY,
    FullName VARCHAR(50),
    ManagerID INT
);

INSERT INTO Employees_2 (EmployeeID, FullName, ManagerID) VALUES
(1, 'John Doe', NULL), 
(2, 'Jane Smith', 1),   
(3, 'Peter Jones', 1),  
(4, 'Emily White', 2),
(5, 'Michael Brown', 2),
(6, 'Chris Green', 4); 

select employee.FullName, manager.FullName from Employees_2 employee LEFT JOIN Employees_2 manager ON employee.ManagerId = manager.EmployeeID;

CREATE TABLE Sales (
    TransactionID INT,
    Store VARCHAR(50),
    SalesAmount DECIMAL(10, 2)
);

INSERT INTO Sales (TransactionID, Store, SalesAmount)
VALUES
    (1, 'A', 100.00),
    (2, 'A', 200.00),
    (3, 'A', 150.00),
    (4, 'B', 250.00),
    (5, 'B', 300.00);

select store, sum(SalesAmount) as sales_amt from Sales group by Store;

-- using window functions

select store, sum(salesamount) over (order by salesamount desc) as total_spend from sales;

select store, salesamount, sum(salesamount) over (partition by store) as sum_spend from sales;

select transactionid, store, salesamount, row_number() over (order by transactionid desc) from sales;

select transactionid, store, salesamount, row_number() over (order by salesamount desc) from sales;

select transactionid, store, salesamount, row_number() over (partition by store order by salesamount desc) from sales;

CREATE TABLE employees3 (
    employee_id serial PRIMARY KEY,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    position    VARCHAR(50),
    salary      DECIMAL(10,2)
);

CREATE TABLE contractors3 (
    contractor_id serial PRIMARY KEY,
    first_name    VARCHAR(50),
    last_name     VARCHAR(50),
    position      VARCHAR(50),
    hourly_rate   DECIMAL(10,2)
);

INSERT INTO employees3 (first_name, last_name, position, salary)
VALUES
('Alice', 'Smith', 'Developer', 70000.00),
('Bob', 'Johnson', 'Developer', 75000.00),
('Charlie', 'Lee', 'Manager', 90000.00);

INSERT INTO contractors3 (first_name, last_name, position, hourly_rate)
VALUES
('Dave', 'Williams', 'Developer', 40.00),
('Eve', 'Brown', 'Tester', 35.00),
('Bob', 'Johnson', 'Developer', 45.00);

select first_name, last_name from employees3 union select first_name, last_name from contractors3;

-- with duplicates, so faster than union which takes time for deduplication
select first_name, last_name from employees3 union all select first_name, last_name from contractors3;

create index idx_phone on customers (phone_number);

explain analyze select phone_number from customers where phone_number = '9876543210';

explain select phone_number from customers;

explain analyze select phone_number from customers;

CREATE TABLE orders6 (
    order_id serial,
    order_date date NOT NULL, 
    customer_name VARCHAR(50),
    amount NUMERIC(10,2)
)
partition by range (year(order_date))(
	partition p_before_2020 values less than (2020),
	partition p_2020 values less than (2021),
	partition p_2021 values less than (2022),
	partition p_2022 values less than (2023),
	partition p_future values less than MAXVALUE
);

CREATE TABLE regex_samples (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_text VARCHAR(100)
);


INSERT INTO regex_samples (sample_text) VALUES 
('apple'),         -- id=1
('Banana'),        -- id=2 (note the capital B)
('cherry'),        -- id=3
('date'),          -- id=4
('elderberry'),    -- id=5
('fig'),           -- id=6
('grape'),         -- id=7
('honeydew'),      -- id=8
('running'),       -- id=9 (ends with "ing")
('123abc');        -- id=10 (starts with digits)

select * from regex_samples where sample_text regexp '^[0-9]';

select * from regex_samples;

-- ^ - must start this way, starts with A or any capital letter and ends with small letter, + - checks for every single character, $ - must end this way
select * from regex_samples where sample_text regexp '^[A-Za-z]+$';

-- searches by occurence of just one character and uses + to group up more
select * from regex_samples where sample_text regexp '^[apple|banana]+$';

-- groups the query and searches -> ()
select * from regex_samples where sample_text regexp '^(apple|banana)$';

select * from regex_samples where sample_text regexp '^[0-9]{3}[A-Za-z]+$';

CREATE TABLE demo_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(50),
    phone VARCHAR(25),
    email VARCHAR(100),
    date_col VARCHAR(10),
    status VARCHAR(20),
    sku VARCHAR(20),
    username VARCHAR(30),
    notes VARCHAR(100)
);


INSERT INTO demo_data (full_name, phone, email, date_col, status, sku, username, notes)
VALUES
-- 1
('John Smith', 
 '123-456-7890', 
 'john@example.com', 
 '2025-02-07', 
 'pending', 
 'ABCD', 
 'johnsmith', 
 'Ships to CA'),

-- 2
('Alice Johnson', 
 '(987) 654-3210', 
 'alice@@example.net', 
 '2025-02-07', 
 'inactive', 
 'SKU-123', 
 'alice', 
 'NY location'),

-- 3
('Bob Williams', 
 '+1-555-123-4567', 
 'bob@sample.org', 
 '20250207', 
 'complete', 
 '1SKU', 
 'bob123', 
 'Shipping to CA'),

-- 4
('Mary 1 White', 
 '(123) 123-4567', 
 'mary123@example.com', 
 '2025-13-31', 
 'PENDING', 
 'abc-999', 
 'mary_white', 
 'Something about CA or'),

-- 5
('Mark-Spencer', 
 '1234567890', 
 'mark@example.com', 
 '2024-11-02', 
 'active', 
 'SKU-9999', 
 'mark', 
 'Random note'),

-- 6
('Jane O''Connor',   -- Note the doubled apostrophe for SQL
 '987-654-3210', 
 'jane.o.connor@example.org', 
 '2024-12-31', 
 'inactive', 
 'ABCDE', 
 'janeO', 
 'Contains CA or NY'),

-- 7
('Invalid Mail', 
 '000-000-0000', 
 'invalid@@example..com', 
 '2023-01-15', 
 'inactive', 
 'XYZ000', 
 'invalid', 
 'Double @ and dots'),

-- 8
('NoSpacesHere', 
 '+12-345-678-9012',
 'nospaces@example.co',
 '2025-02-07',
 'pending',
 'SKU999',
 'NoSpaces',
 'Ends with .co domain');
 
 select * from demo_data;
 
 select * from demo_data where full_name regexp '^[A-Za-z ]+$'; 
 
 CREATE TABLE Accounts (
  AccountID INT PRIMARY KEY,
  AccountHolder VARCHAR(100),
  Balance DECIMAL(10,2)
);

-- Insert a new record into Accounts
INSERT INTO Accounts (AccountID, AccountHolder, Balance)
VALUES (1, 'Alice', 5000.00);

begin;

update Accounts set Balance = Balance - 1000 where AccountID = 1;
select * from Accounts;

rollback;
commit;
rollback; -- no use as we already commited the values

start transaction; -- either begin / transaction
update Accounts set AccountHolder = 'Mathew' where AccountID = 1;

select * from Accounts;
rollback;
select * from Accounts;

commit;