
-- contact info type fname, lname, email


create type contact_info as (
    fname varchar(40), 
    lname varchar(40), 
    email varchar(100)
);


-- display all types in the database ? 

-- use type to create table

create table engineers (
    id serial primary key,
    info contact_info ,
    sep text
);


---------------------


Alter table tablename rename to newname; 

alter table engineers rename to engs;



alter table engs add column salary money ; 


alter table engs drop column salary  ; 


-- add foreign key constraint after creation table?


alter table engs 
add column dept_id int references depts(id);


alter table engs
add column d_id int ; 

add constraint dept_engs_fk
foreign key (d_id)
references depts(id);

add constraint dept_engs_fk
foreign key (d_id)
references depts(id) on update cascade  on delete set null ;

alter table engs 
add constraint dept_engs_fk
foreign key (d_id)
references depts(id) on update set null  on delete cascade ;


alter table engs 
drop constraint dept_engs_fk;



--- rename column

alter table engs 
rename column d_id to department;

-----------------------------------------------------------

--- DML 
----- insert 

-- insert data in all table columns 

insert into tablename values (values for all columns in the table);


insert into depts values (1, 'python');

--- insert data in sepcif fields

insert into tablename (colmns names) values (val1, val2, ....); 


insert into depts (id) values (6);



insert into engs (id , sep) values (100 , 'ce');


insert into engs ( sep) values ( 'AI');


---------------------------------------
-- insert with composite datatypes 


insert into engs (info) values (row('ahmed', 'Mohamed', 'mm@gg.com'));



insert into engs (info.fname) values ('ahmed');


--- update 

update tablename set colnames = value , colname= values
where id = 1
;

update engs set dept_id=1 ;

update engs set dept_id=3 where id%2==0 ;


update engs set info=row('abc', 'abc', 'abc') where id = 5;

update engs set info.fname='updated' where id = 2;


--- delete 


delete from engs;

delete from engs where id = 100;
-- truncate 
truncate table tablename ; --remove all rows from the table at one step 




--------------------------  DML   ---------------

select * , fields 
from tablename
[where condition]
[group by fields]
[having condition]
[order by  column]
[limit no_of_rows];


select * from engs;

select info , sep from engs;

-- alias column
select info as emp_info , sep from engs;


-- select fname only 
 select (info)fname from engs;

 -------------------- where clause 

 select * from engs where id = 7;
 select * from engs where id > 7;
 select * from engs where sep is null;
 select * from engs where sep is not null;
 -- select data that matches specific pattern 
 -- (regex , regurlar expressions)

select * from engs where (info).fname like 'a%';
-- % --> zero or more
-- underscore _ --> exactly one 




select * from engs where id+5> 15 and id%2=0;


-- in operator  --> get values  exact match the given values 

select * from engs where id in (6, 10);  


--> what about range 
select * from engs where id between 6 and 10;


---------------Aggregation functions--------------------
-- min , max, avg, count , sum -->return one value
--- are not allowed to be used in where clause 

select sum(id) from engs;

-- use the aggregations function to get no of engineers in each dept? 


-- apply commualative action and return with result divided into 
-- parts according to field 

select count(*) from engs ; 

3 ---. dept1 , 3 dept2 , 3 dept 3

select count(*) from engs group by dept_id; 

-- in this case only you can put the dept_id in the select clause


select count(*), dept_id from engs group by dept_id; 

---- get 


select count(*), dept_id from engs
group by dept_id
having count(dept_id)> 2; 

-- how the data are being ordered in postgres 

-- postgres --> data are ordered by updated status 



select * from engs order by id; 

--- limit ? 

select * from engs order by id limit 2; 

--- sub query 

select * from engs
 where dept_id = (select id from depts where name='ai');


----------------------- joins 

select * 
from engs, depts;   -- catesian product

-- inner join 
select * from engs , depts 
where engs.dept_id = depts.id;


select * from engs
inner join depts 
on  engs.dept_id = depts.id;



select * from engs
left join depts 
on  engs.dept_id = depts.id;





select * from engs
right join depts 
on  engs.dept_id = depts.id;





























































































--- to select all data from any table
select * from depts;

















































