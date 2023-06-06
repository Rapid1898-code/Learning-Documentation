


---
## Installation MYSQL
<br>Installation
```markdown
https://www.youtube.com/watch?v=GIRcpjg-3Eg
```



---
## SELECT, FROM
<br>Outputs all columns from the table customer (automatically sorted by id)
```markdown
select * from customer
```
Outputs only the column firstname (no sorting)
```markdown
select firstname from customer
```
Outputs 2 columns firstname and lastname
```markdown
select firstname, lastname from customer
```



---
## DISTINCT, WHERE, BETWEEN, IN
<br>With distinct the output occurs only one time if the firstname is the same
```markdown
select distinct firstname from customer
```
Everything will be outputed cause the id is unique
```markdown
select distinct id,firstname from customer
```
Only when firstname and lastname are equal there will be no outputs
```markdown
select distinct firstname,lastname
```

<br>Outputs the row with the id = 0
```markdown
select * from customer
    where id = 0
```

<br>Outputs all rows where the firstname is Janet
```markdown
select * from customer
    where firstname = 'Janet'
```

<br>Outputs all streets which are in the city of Oslo
```markdown
select street from customer
    where city = 'Oslo'
```

<br>all IDs >= 40
```markdown
...where id >= 40
```
all IDs except 40 (in some DBs you have to use instead !=)
```markdown
...where id <> 40
```
everything between 40 and 50
```markdown
...where id between 40 and 50
```
some values are checked for id
```markdown
...where id in (43,44,45)
```



---
## AND, OR, ORDER BY, ASC, DESC
Outputs all rows where id >= 40 and firstname is Robert
```markdown
select * from customer
where id >= 40
and firstname = "Robert"
```

<br>One of the both conditions have to be fullfilled
```markdown
...where id >= 40 or firstname = "Robert"
```
combinaton of logical or and and (better to use parantheses)
```markdown
...where id >= 40 or firstname = "Robert" and lastname = "Fuller"
```

<br>Outputs rows >=40 sorted ascending for firstname and lastname
```markdown
select * from customer
where id >= 40
order by firstname, lastname asc
```

<br>Output in descending order
```markdown
...order by firstname, lastname desc
```



---
## INSERT, INTO, VALUES, UPDATE, SET, DELETE
Inserts row in the table with specific values for the columns
```markdown
insert into customer
values (50, 'James', 'Karsen', '107 Upland Pl.', 'Dallas')
```

<br>Inserts row  with streetname = NULL (this is not working for key-columns like id)
```markdown
insert into customer (id, firstname, lastname, city)
values (51, 'James', 'Karsen', 'Dallas')
```

<br>Update the row with the id = 51 regarding street
```markdown
update customer
set street = '547 Seventh Av.'
where id = 51
```

<br>Update the strett where firstname James and lastname Karsen
```markdown
...where firstname = 'James' and lastname = 'Karsen'
```

<br>Delete row with the id = 51
```markdown
delete from customer
where id = 51
```



---
## NULL, LIKE, TOP, LIMIT, ROWNUM, PERCENT
<br>Outputs the first 5 results (depending on the sorting)
```markdown
select top 5 * from customer
```

<br>in some DBs also in the following form - oututs the first 10 results
```markdown
select * from customer
limit 10
```

<br>and also in this form in some DBs
```markdown
select * from customer
where rownum <= 10
```

<br>Outputs 10 top percent of the results
```markdown
select top 10 percent * from customer
```

<br>"_" will be replaced with one char - so the output will be done for eg. Oslo or Oxlo
```markdown
select * from computer
where city like 'O_lo'
```

<br>Outputs all entries which end with "lo" for the column city
```markdown
... where city like '%lo'
```
Outputs all entries which start with 2 chars and then the char "l"
```markdown
... where city like '__l%'
```
When there sould be a serach for the percent sign "%" - this has to be masked with \%
```markdown
... where city like '__l\%'
```

<br>Outputs all rows where lastname is NULL
```markdown
select * from computer
where lastname is NULL
```

<br>Outputs all rows where there is some entry in the column lastname
```markdown
where lastname is NOT NULL
```



---
## IN
IDs will be selected from the rechnungen-table and will be used for the aboth where-clausel for select *
```markdown
select * from customer
where id IN
        (select id from rechnungen
        where date <=3)
```



---
## Tables and Data-Types
CREATE, TABLE, INT, VARCHAR, BINARY, BOOLEAN, VARBINARY, SMALLINT, BIGINT, DECIMAL, NUMERIC, DATE, TIME

<br>Create a new table with name Rechnung
```markdown
create table Rechnung
    (
    RechnungsID int,
    CustomerID, int,
    Betrag int
    )
```

<br>Insert a row in the new table Rechnung with specific values
```markdown
insert into Rechnung values (1,0,50)
```
Integer
```markdown
value INT
```
variable Character
```markdown
name VARCHAR(255)
```
Bits
```markdown
bin BINARY (255)
```
Bool (TRUE / FALSE)
```markdown
bool BOOLEAN
```
variable Bits
```markdown
VARBINARY(255)
```
SmallInt
```markdown
SMALLINT
```
BigInt
```markdown
BIGINT
```
Decimal Number (total,decimal places) - 3 beforce decimal places, 2 decimal places
```markdown
DECIMAL (5,2)
```
Numeric Number
```markdown
NUMERIC (5,2)
```
Floating Number
```markdown
FLOAT (10)
```
Double Precision
```markdown
DOUBLE PRECISION
```
Date value
```markdown
DATE
```
Time value
```markdown
TIME
```
Timestamp value
```markdown
TIMESTAMP
```



---
## Primary und Foreign Keys, not null
DROP, UNIQUE, NOT NULL, PRIMARY KEY, FOREIGN KEY, REFERENCES<br>
Drop whole table
```markdown
drop table Rechnung IF EXISTS
```

<br>RechnungID is a mandatory field - must be allways available and not empty with NULL - with UNIQUE the ID has to be unique
<br>Define the Primary Key with PRIMARY KEY
<br>Define the Foreign Key with FOREIN KEY (Primary Key in anderer Tabelle) - is referencing to the id in the customer table
```markdown
create table Rechnung
    (
    RechnungsID int NOT NULL UNIQUE
    CustomerID int NOT NULL
    Betrag int NOT NULL
    PRIMARY KEY(RechnungsID)
    FOREIGN KEY(CustomerID) REFERENCES Customer(ID)
    )
```


---
## Change Tables, Autoincrement
AUTO_INCREMENT, DEFAULT, IDENTITY, ALTER TABLE, ADD, DROP COLUMN, ALTER COLUMN
<br>With AUTO_INCREMENT the id will be given automatically - starts with 1 and then ascending (e.g. MYSQL)
<br>In some DBs with: RechnungsID int IDENTITY(0,1) (e.g. MSSQL)
<br>In some DBs with: RechnungsID int IDENTITY (e.g. HSQL)
<br>Using DEFAULT - when something is inserted without specific value - 50 will be used as default value
```markdown
create table Rechnung
    (
    RechnungsID int NOT NULL AUTO_INCREMENT
    CustomerID int NOT NULL,
    Betrag int DEFAULT 50,
    PRIMARY KEY(RechnungsID),
    FOREIGN KEY(CustomerID) REFERENCES Customer(ID)
    )
```

<br>change table Rechnung
```markdown
alter table Rechnung
```
add datum-column with datatype date
```markdown
add Datum Date
```
drop column betrag from the table
```markdown
drop column betrag
```
change column to VARCHAR(255)
```markdown
alter column VARCHAR(255)
```



---
## Joins
INNER JOIN, ON, LEFT JOIN, RIGTH JOIN, FULL JOIN
<br>Outputs firstname + lastname from all customers which exists in the rechnung table
```markdown
select firstname, lastname from customer
where id in (select customerID from rechnung)
```

<br>Outputs all attributes from the customers, which have a rechnung (same as aboth - but for all attributes)
```markdown
select *
from customer
inner join Rechnung
on customer.ID = rechnung.customerID
```

<br>Outputs all elements from the left table (customer) - where in the table Rechnung something is inside it will be outputed
```markdown
...left join Rechnung
```
Outputs alle elements from the right table (Rechnung) - with informations from both tables
```markdown
...right join Rechnung
```
Outputs everything from both sides
```markdown
...full join Rechnung
```


---
## SQL Built In Funktionen
AVG, COUNT, TOP,  FIRST, LIMIT, LAST, UCASE, UPPER, LCASE, LOWER<br>
Outputs the average
```markdown
select avg(betrag) from rechnung
```
Returns the count of the rows
```markdown
select count(rechnungID) from rechnung
```

<br>Outputs the count of the rechnungIDs where the betrag is >= the average in the rechnungs table
```markdown
select count(rechnungID) from rechnung
where betrag >= (select AVB(betrag) from rechnung)
```

<br>Outputs maximum betrag from the table
```markdown
select max(betrag) from rechnung
```
Outputs the minimum betrag from the table
```markdown
select min(betrag) from rechnung
```
Outputs the sum betrag from the table
```markdown
select sum(betrag) from rechnung
```
Outputs the firstname as uppercase - sometimes also upper(firstname)
```markdown
select ucase(firstname) from customer
```
Outputs the firstname as lowercase - sometimes also lower(firstname)
```markdown
select lcase(firstname) from customer
```
Outputs the length of the string
```markdown
select len(firstname) from customer
```
Outputs the actual date + time
```markdown
select now() from  customer
```





































