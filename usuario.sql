drop database usuario;
create database usuario;

create user 'ing'@'localhost' identified by 'Developer123!';

grant all privileges on usuario.* to 'ing'@'localhost'
with grant option;

use usuario;

CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `contrasenia` varchar(64) NOT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;