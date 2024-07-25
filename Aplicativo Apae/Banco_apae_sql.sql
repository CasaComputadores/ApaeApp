create database apae;
use apae;

create table doadores(
id int primary key not null auto_increment,
ativo int not null ,
tipo varchar(50) not null,
nome varchar(50) not null,
endereco varchar(50) not null,
bairro varchar(50) not null,
celular varchar(20),
valor varchar(20) not null,
numero int not null
);

select * from doadores;
drop table doadores;