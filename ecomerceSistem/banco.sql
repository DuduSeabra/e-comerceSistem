DROP DATABASE IF EXISTS comprasonline;
create database comprasonline;

use comprasonline;

create table cadastros (

nome varchar(50) not null primary key,
senha varchar(25),
usuarioweb varchar(5),
status_cliente varchar(30),
nivel int

);
insert into cadastros (nome, senha, usuarioweb, status_cliente, nivel) values ("admin", "1234", "sim", "admin", "2");

create table produtos(

id_produto int not null primary key auto_increment,
nome varchar(80),
marca varchar(20),
departamento varchar(50),
preco float

);

create table pedidos(
id_pedido int not null primary key auto_increment,
fk_nome varchar(50) not null,
status_pedido varchar(50)

);

ALTER TABLE `comprasonline`.`pedidos` 
ADD CONSTRAINT `fk_nome`
  FOREIGN KEY (`fk_nome`)
  REFERENCES `comprasonline`.`cadastros` (`nome`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

create table pedidoitem(

fk_id_pedido int not null,
fk_id_produto int not null

);

ALTER TABLE `comprasonline`.`pedidoitem` 
ADD CONSTRAINT `fk_id_pedido`
  FOREIGN KEY (`fk_id_pedido`)
  REFERENCES `comprasonline`.`pedidos` (`id_pedido`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `comprasonline`.`pedidoitem` 
ADD CONSTRAINT `fk_id_produto`
  FOREIGN KEY (`fk_id_produto`)
  REFERENCES `comprasonline`.`produtos` (`id_produto`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

create table pagamento(

id_pagamento int not null primary key auto_increment,
fk_id_pedido_pagamento int not null

);

ALTER TABLE `comprasonline`.`pagamento` 
ADD CONSTRAINT `fk_id_pedido_pagamento`
  FOREIGN KEY (`fk_id_pedido_pagamento`)
  REFERENCES `comprasonline`.`pedidos` (`id_pedido`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
create table carrinho(

id_carrinho int not null primary key auto_increment,
fk_nome_carrinho varchar(50) not null

);

ALTER TABLE `comprasonline`.`carrinho` 
ADD CONSTRAINT `fk_nome_carrinho`
  FOREIGN KEY (`fk_nome_carrinho`)
  REFERENCES `comprasonline`.`cadastros` (`nome`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


create table carrinhoitem(

fk_id_carrinho int not null,
fk_id_produto_carrinho int not null

);

ALTER TABLE `comprasonline`.`carrinhoitem` 
ADD CONSTRAINT `fk_id_carrinho`
  FOREIGN KEY (`fk_id_carrinho`)
  REFERENCES `comprasonline`.`carrinho` (`id_carrinho`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `comprasonline`.`carrinhoitem` 
ADD CONSTRAINT `fk_id_produto_carrinho`
  FOREIGN KEY (`fk_id_produto_carrinho`)
  REFERENCES `comprasonline`.`produtos` (`id_produto`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

insert into pedidos (fk_nome, status_pedido) values ("aaaaa", "em wjen");
insert into pedidoitem (fk_id_pedido, fk_id_produto) values ("2", "1");

select * from pedidos where fk_nome = "aaaaa";
select * from produtos;