USE EdutechDB;

select * from Professores;

select * from Alunos;

select * from Alunos alu
    inner join Professores pro
    on alu.Professor = pro.Nome

select * from Alunos where Nome like '%Doglas%'
