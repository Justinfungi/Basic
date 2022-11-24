sudo mysql


create database Justris
show databases
use Justris
create table GG
insert into GG values (1, "Greeting", "yo");


#data manipulation

#Update
update avengers set beard =True where first_name = "thor";


#Data Query

  #Select
    #retrive
    select * from GG;
    #condition
    select * from GG where branch = "Greeting" or id < 30;
    #oder
    select * form GG order by age asc(desc)






#add attribute
alter table avengers add beard boolean;
