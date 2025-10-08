create database internshala;
show databases;

use internshala;

create table employe ( emp_id int, emp_name varchar(15), salary float);  
show tables;

select * from employe;

insert into employe values  (1, "Ajay", 100000);

insert into employe values (2, "Harry", 90000), (3, "Rahul", 75000), (4, "Just Now", 75000);
 
 select * from employe;