SELECT SUM(COST) FROM PETRESCUE;

SELECT SUM(COST) as SUM_OF_COST FROM PETRESCUE;

SELECT MAX(QUANTITY) FROM PETRESCUE;

SELECT AVG(COST) FROM PETRESCUE;

SELECT AVG(COST / QUANTITY) FROM PETRESCUE WHERE ANIMAL = "Dog" ;

SELECT ROUND(COST) FROM PETRESCUE;

SELECT LENGTH(ANIMAL) FROM PETRESCUE;

SELECT UCASE(ANIMAL) FROM PETRESCUE;

SELECT DISTINCT(UCASE(ANIMAL)) FROM PETRESCUE

SELECT LCASE(ANIMAL) FROM PETRESCUE WHERE ANIMAL = 'cat' 

select DAY(RESCUEDATE) from PETRESCUE where ANIMAL = 'Cat' 

select SUM(QUANTITY) from PETRESCUE where MONTH(RESCUEDATE)='05';

select SUM(QUANTITY) from PETRESCUE where DAY(RESCUEDATE)='14';

select (RESCUEDATE + 3 DAYS) from PETRESCUE;

select (CURRENT DATE - RESCUEDATE) from PETRESCUE;

select * from employees where JOB_ID IN (select JOB_IDENT from jobs);

select * from employees where JOB_ID IN (select JOB_IDENT from jobs where JOB_TITLE= 'Jr. Designer');

select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT from jobs where JOB_IDENT IN (select JOB_ID from employees where SALARY > 70000 );

select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT from jobs where JOB_IDENT IN (select JOB_ID from employees where YEAR(B_DATE)>1976 );

select JOB_TITLE, MIN_SALARY,MAX_SALARY,JOB_IDENT from jobs where JOB_IDENT IN (select JOB_ID from employees where YEAR(B_DATE)>1976 and SEX='F' );

select * from employees, jobs;

select * from employees, jobs where employees.JOB_ID = jobs.JOB_IDENT;

select * from employees E, jobs J where E.JOB_ID = J.JOB_IDENT;

select EMP_ID,F_NAME,L_NAME, JOB_TITLE from employees E, jobs J where E.JOB_ID = J.JOB_IDENT;

