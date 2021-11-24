CREATE DATABASE EdutechDB;

USE EdutechDB;

CREATE TABLE test (
    a int not null
);

CREATE TABLE Professores (
    Nome VARCHAR(100) NOT NULL PRIMARY KEY,
    Email VARCHAR(100) NOT NULL,
    Turmas 
);

CREATE TABLE Alunos (
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Turma VARCHAR(50) NOT NULL,
    CGM INT NOT NULL,
    TURNO CHAR NOT NULL,
    Status_ BIT NOT NULL
    Professor 
);
