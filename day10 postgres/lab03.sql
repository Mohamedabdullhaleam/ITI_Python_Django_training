SELECT * FROM student;
--- add gender  & enum male and female
-- creating the enum --
CREATE TYPE gender_enum AS ENUM ('male', 'female');
--(1)--- altering the table to add gender 
ALTER TABLE student
ADD gender gender_enum;
--(2) -- add birth day 
ALTER TABLE student
ADD birth_date DATE;
--(3)-- delete the name column 
ALTER TABLE student
DROP COLUMN name;
--two columns first name and last name.
ALTER TABLE student
ADD f_name VARCHAR(20),
ADD l_name VARCHAR(20);
--(4)-- Delete the address and email column and replace it with contact info (Address, email) as object/Composite Data type.
-- creating the composite contact
create type contact_info as (
    adress varchar(40), 
    email varchar(100)
);
ALTER TABLE student 
ADD contact_info contact_info;
--(5)--Change any Serial Datatype at your tables to smallInt

-- Step 1: Add a new SMALLINT column
ALTER TABLE student
ADD new_id SMALLINT;
-- Step 2: Copy data from the SERIAL column to the new SMALLINT column
UPDATE student
SET new_id = track_id;
-- Step 3: Drop the SERIAL column
ALTER TABLE student
DROP COLUMN track_id;
-- Step 4: Rename the new SMALLINT column to the original name
ALTER TABLE student
RENAME COLUMN new_id TO track_id;

--6--Add/Alter foreign key constrains in Your Tables.--
alter table student 
add column foreign_id int references student(student_id);
--7--Insert new data in all Tables.
INSERT INTO student (student_id,gender,birth_date,f_name,l_name)
VALUES (5,'male','1992-10-01','mazen','Mohamed');
-- 8-- displaying stds info 
SELECT * FROM student ;
--9--   display men only
select * from engs where gender = 'male'; 
--10-- number of female students
select count(*) from student
group by gender
having gender = 'male'; 
--11 --Display the students who are born before 1992-10-01.
select * from student where birth_date = '1992-10-01'; 
--12--
select * from student where birth_date = '1992-10-01' and gender='male'; 
--13--Display subjects and their max score sorted by max score.
INSERT INTO subject (subject_id,subject_name,description,max_score,track_id)
VALUES (1,'java','prog','100','3');
INSERT INTO track (track_id,track_name)
VALUES ('1','python');
-- 13-- disply by max scores
select * from subject order by max_score; 
--14--Display the subject with highest max score
SELECT * FROM subject
ORDER BY max_score DESC
LIMIT 1;
--Display students’ names that begin with A.--
SELECT f_name
FROM student
WHERE f_name LIKE 'A%';
--16--Display the number of students’ their name is “Mohammed”
SELECT count(*) FROM student
having f_name like 'mazen';
select count(*), f_name from student
group by f_name
having f_name like 'mazen'; 
--17--17. Display the number of males and females. 
SELECT gender, COUNT(*) as count
FROM student
GROUP BY gender;
--18--Display the repeated first names and their counts if higher than 2. 
SELECT f_name, COUNT(*) AS name_count
FROM student
GROUP BY f_name
HAVING COUNT(*) > 2;


