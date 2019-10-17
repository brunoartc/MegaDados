CREATE TABLE Joinhas (
    Reacao INT NOT NULL DEFAULT 0,
    PostId INT NOT NULL,
    IdUsuario int NOT NULL,
    PRIMARY KEY (IdUsuario, PostId),
    FOREIGN KEY (IdUsuario) 
        REFERENCES Usuarios(Id),
    FOREIGN KEY (PostId)
        REFERENCES Post (Id)
);