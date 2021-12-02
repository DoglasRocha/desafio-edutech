USE EdutechDB;
DELETE Alunos WHERE Nome='Doglas'

select * from Professores;

select * from Alunos;

select alu.Nome, alu.Email, alu.Professor from Alunos alu
    inner join Professores pro
    on alu.Professor = pro.Nome
    and pro.Nome = 'Paulo'

select * from Professores where Nome like '%Alberto%'
