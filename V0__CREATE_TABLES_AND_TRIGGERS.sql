#DROP DATABASE IF EXISTS MD;

#CREATE DATABASE MD;
USE MD;


DROP TABLE IF EXISTS Preferencias;

DROP TABLE IF EXISTS Tags;
DROP TABLE IF EXISTS Post;
DROP TABLE IF EXISTS Usuarios;

CREATE TABLE Usuarios (
    Id int AUTO_INCREMENT,
    Nome varchar(255) NOT NULL,
    Email varchar(255) UNIQUE,
    Cidade varchar(255) NOT NULL,
    PRIMARY KEY (Id, Email)
);

CREATE TABLE Preferencias (
    PassaroNome VARCHAR(255),
    IdUsuario int NOT NULL,
	PRIMARY KEY (IdUsuario, PassaroNome),
    FOREIGN KEY (IdUsuario) REFERENCES Usuarios(Id)
);

CREATE TABLE Post (
    Id INT AUTO_INCREMENT,
    IdUsuario INT NOT NULL,
    Titulo VARCHAR(255) NOT NULL,
    Url VARCHAR(255) NOT NULL,
    Texto VARCHAR(255),
    Existe int DEFAULT 1,
    PRIMARY KEY (Id),
    FOREIGN KEY (IdUsuario)
        REFERENCES Usuarios(Id)
);

CREATE TABLE Tags (
    Typee INT,
    PostId INT NOT NULL,
    Conteudo VARCHAR(255) NOT NULL,
    Existe VARCHAR(255),
    PRIMARY KEY (Typee , PostId , Conteudo),
    FOREIGN KEY (PostId)
        REFERENCES Post (Id)
);

DELIMITER $$
CREATE TRIGGER Post_check BEFORE UPDATE ON Post
FOR EACH ROW
BEGIN
	UPDATE Tags SET Existe = NEW.Existe WHERE
		PostId = NEW.Id;
END$$
DELIMITER ;

