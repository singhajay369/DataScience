use world;

select * from city;

-- task 1: Extract the city data where city name ends with port

select * from city where name like '%port';

-- task2 : extract the city name start with 'A' and end with "garh"

select * from city where name like 'a%garh';

-- task3: extract the city with 4 character as p

select * from city where name like '___p%';
