sudo mysql
sudo mysql -u fish -p

# user
117


To list users:

select user,host from mysql.user;
To show privileges:

show grants for 'user'@'host';
To change privileges, first revoke. Such as:

revoke all privileges on *.* from 'user'@'host';
Then grant the appropriate privileges as desired:

grant SELECT,INSERT,UPDATE,DELETE ON `db`.* TO 'user'@'host';
Finally, flush:

flush privileges;
The MySQL documentation is excellent:




# create
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
