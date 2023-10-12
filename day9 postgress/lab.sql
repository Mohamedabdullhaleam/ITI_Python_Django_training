CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    track_id int,
    Foreign key(track_id) references Track(track_id),
);


CREATE TABLE Track (
    track_id INT PRIMARY KEY,
    track_name VARCHAR(100)

);

CREATE TABLE Subject (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(50),
    description TEXT,
    max_score INT,
    track_id int,
    Foreign key(track_id) references Track(track_id)

);

CREATE TABLE studies (
    exam_id INT PRIMARY KEY,
    Date Date NOT null,
    student_id int,
    subject_id int, 
    Foreign key(student_id) references student(student_id),
    Foreign key(subject_id) references Subject(subject_id),
    score INT

);

CREATE TABLE contact_info (
   student_id int,
   Foreign key(student_id) references student(student_id),
    email char(100),
    address char(100)
);