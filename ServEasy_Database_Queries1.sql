# Run these queries in MySQL

create database ServEasy; #Creating database
use ServEasy; #Using Database

CREATE TABLE ServiceProviders( #Creating table for Service Providers
spid int, #unique service provider id
category varchar(5) not null, #category of service providers CA-->Capenters EL-->Electricians PL-->Plumbers BW-->Beauticians for women SM-->Salon for men
address varchar(75) not null, #address of service provider 
sp_name varchar(75) not null, #service provider's name
email varchar(50) not null, #email of service provider
pwd varchar(50) not null, #password of service provider
contact_no varchar(11) not null, #contact number of service provider
constraint pk_sp primary key (spid) #spid is primary key
);

CREATE TABLE Services( #Creating services table
sid int, #unique service id
category varchar(5) not null, #category of service
dscrptn varchar(300), #description of service
constraint pk_services primary key (sid) #sid is primary key
); 

CREATE TABLE Provides( #Creating Provides table
sid int auto_increment not null , #unique service id
spid int, #unique service provider id
constraint pk_provides primary key (sid,spid), #(sid,spid) is primary key
constraint fk_provides1 foreign key (sid) references Services(sid), 
constraint fk_provides2 foreign key (spid) references ServiceProviders(spid)
);

CREATE TABLE Customers(
cid int auto_increment, #unique customer id
email varchar(50) not null, #customer's email
pwd varchar(30) not null, #password
address varchar(75) not null, #address of customer
c_name varchar(75) not null, #name of customer
contact_no varchar(11) not null, #contact number of customer
constraint pk_customers primary key (cid) #cid is primary key
);

CREATE TABLE Bookings(
cid int not null, #unique customer id
bid int not null auto_increment, # unique booking id
spid int, # unique service provider id
timing int not null,  #24 hour format # hour/minutes/seconds
category varchar(5) not null, #category of service provider
`status` char(1) not null,  #status of booking C-->cancelled D-->Done B-->Booked 
constraint fk_bookings1 foreign key (cid) references Customers(cid),
constraint fk_bookings2 foreign key (spid) references ServiceProviders(spid),
constraint pk_bookings1 primary key (bid) #bid is primary key
);

CREATE TABLE BOOKEDFOR(
bid int not null, #booking id
sid int not null, #service id
constraint fk_bookedfor1 foreign key (sid) references Services(sid),
constraint fk_bookedfor2 foreign key (bid) references Bookings(bid),
constraint pk_bookedfor primary key (sid,bid) #primary key is a combination of sid and bid
);

alter table ServiceProviders 
rename to ServiceProvider;  #ServiceProviders table renamed to ServiceProvider
alter table Customers
rename to Customer;   #Customers table renamed to Customer

alter table Customer add column loggedin bool default False;
alter table Services
rename to Service;    #Services table renamed to Service
alter table Bookings
rename to Booking;   #Bookings table renamed to Booking

insert into ServiceProvider #Populating ServiceProvider table
values(1,'CA','12-A Preet Vihar, New Delhi','Amit Sharma','amit007@gamil.com','sharma007','8763456178'),
(2,'CA','B-109 Kalkaji, New Delhi','Brijesh Mathur','bjmt2244@gmail.com','mathurbrijesh','7645378279'),
(3,'EL','D-36 Govindpuri, New Delhi','Dinesh Dhingra','ddmdjt@gmail.com','ddrocksdd','8935325369'),
(4,'EL','KM-89-B Hauz Khas, New Delhi','KD Pathak','kdfromadalat@gmail.com','sonytvbest','8967092339'),
(5,'PL','D-110 Geeta Colony, New Delhi','Sanjeev Verma','sanjeevcool7@gmail.com','sanjeevhartman','7841478916'),
(6,'PL','M-249 Greater Kailash, New Delhi','Chandan Thakur','chanduchaiwala@gmail.com','chandufromtkss','9372658267'),
(7,'BW','7A-124 Jahangirpuri, New Delhi','Cheshtha Trehan','cheshtha00@gmail.com','trehancheshtha','9329479183'),
(8,'BW','DP-28 Russian embassy road, New Delhi','Shanice Shreshtha','shanicenikhil@gmail.com','shanicenikhil','8365921311'),
(9,'SM','114-C CR park road, New Delhi','Adil Rashid','adilrashid03@gmail.com','adilfromengland','9451320909'),
(10,'SM','22-F Netaji Subhash Place, New Delhi','Imran Khan','imranpk@gmail.com','imranpkmkb','8341567091');

select *
from ServiceProvider; #Displaying ServiceProvider

insert into Service #Populating Service table
values(1,'CA','Repair a table, chair, rack, sofa, etc'),
(2,'CA','Make customised furniture'),
(3,'EL','Repair Aplliances'),
(4,'EL','Wiring, fitting/installation of any electrical component'),
(5,'PL','Repair of pipelines, taps, sanitary equipments, etc'),
(6,'PL','Installation of new pipelines, taps, sanitary equipments'),
(7,'BW','Bridal makeup'),
(8,'BW','Manicure, pedicure, makeup, facial, bleeching, etc'),
(9,'SM','Haircut, Shaving Beard, etc'),
(10,'SM','Facial, Bleeching, massage, etc');

select *
from Service; #Displaying Service Table 

insert into Provides  #Populating Provides Table
values(1,1),
(1,2),
(2,1),
(2,2),
(3,3),
(3,4),
(4,3),
(4,4),
(5,5),
(5,6),
(6,5),
(6,6),
(7,7),
(7,8),
(8,7),
(8,8),
(9,9),
(9,10),
(10,9),
(10,10);

select *
from Provides;  #Displaying Provides table

insert into Customer #Populating Customer table
values(1,'vaibhav78@gmail.com','vaibhavag6161','D-111-D Shakarpur, New Delhi','Vaibav Agarwal','8279813538'),
(2,'rmcg2006@gmailcom','rmcgchaitanya','B-110 Kalkaji, New Delhi','Chaitanya Krishna', '6283565012'),
(3,'rmcg2009@gmail.com','rmcggaurang','TA-4 Vasantkunj, New Delhi','Gaurang Krishna','9173518361'),
(4,'ssnehal01@gmail.com','snehsnehal','L-12 Govindpuri, New Delhi','Snehal Singh','8252710154');

select *
from Customer; #Displaying Customer Table

insert into Booking (cid,spid,timing,category,`status`) #Populating Booking table, all columns except bid are populated because is automatically incemented
values(1,3,1300,'EL','D'), 
(1,9,1430,'SM','B'),
(2,5,1000,'PL','D'),
(3,1,0900,'CA','D'),
(4,8,1100,'BW','D');

select *
from Booking;  #Displaying Booking table 

insert into Booking (cid,spid,timing,category,`status`) #inserting one entry in Booking table
values(4,9,1200,'BW','C');

alter table BOOKEDFOR
rename to BookedFor; #BOOKEDFOR table has been renamed to BookedFor, although it doesn't make any difference because SQL is not case sensitive

insert into BookedFor  #Populating BookedFor table
values(1,3),
(2,9),
(3,5),
(4,1),
(5,8),
(6,8);

select *
from BookedFor;  #Displaying BookedFor table