

-- this is a comment in sql 
-- 1- display connection info ?

\conninfo 



-- display available databases on postgres dbms 
\l --> list all dbs 


   Name    |  Owner   | Acceot connection |by default
-----------+----------+----------+-----------------+----------------------------+----------------------------+------------+-----------+-----------------------
 postgres  | postgres | accept connection     | empty
 template0 | postgres | doesnot accept connection     | 
 template1 | postgres | accpet connection     | empty



-- to connect to any db. 
\c dbname;
\c template1;

-- diplay content in the db 
\d




-------- use SQL queries to apply changes on the database 

-- DDL

-- to clear screen 
\! cls

--- 1- create database 

create database dbname;
create database stpy233;

--when use query create database ..  make copy from db template1;

create database dbname template template1;

create database dbname template postgres;

create database dbname template template0;


--- to drop database 
drop database dbname;

-------------- create type

create type gender as enum('male', 'female');


create table depts(id int primary key, name char(40) unique);


create table employees 
(id int , name char(40), email varchar(100) unique , 
gender gender not null, 
salary money default 1000, bdate date, activation timestamp, hours time,
dept_id int ,
primary key(id), 
foreign key (dept_id) references depts(id)
);



--- when create table with columns you may need to sepecify constraint ? 



























