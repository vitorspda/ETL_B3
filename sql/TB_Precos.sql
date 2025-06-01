USE ETL_B3;

GO

CREATE TABLE Precos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    id_ativo INT FOREIGN KEY REFERENCES Ativos(id),
    data DATE NOT NULL,
    preco_abertura DECIMAL(18,4),
    preco_fechamento DECIMAL(18,4),
    maxima DECIMAL(18,4),
    minima DECIMAL(18,4),
    volume BIGINT
);