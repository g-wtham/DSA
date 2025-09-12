select count(*) from vcet_data.vcet_24;

select * from vcet_24 order by salary_decimal desc;

-- alter table vcet_24 rename column `Name of student placed  with his/her contact details` to student_name;
-- alter table vcet_24 rename column `Programme completed` to `branch`;
-- alter table vcet_24 rename column `Name of the  employer with contact details` to `company_name`;
-- ALTER TABLE vcet_24 RENAME COLUMN `Pay package at the time of appointment` TO annual_pay;

SELECT student_name, company_name, annual_pay, salary_decimal FROM vcet_24 ORDER BY salary_decimal DESC;


alter table `vcet_24` add column `salary_decimal` decimal(10, 2);

SET SQL_SAFE_UPDATES = 0;

alter table vcet_24 modify column salary_decimal double;

update vcet_24 set salary_decimal = cast(regexp_replace(annual_pay, '[^0-9.]', '') as double);

update vcet_24 set salary_decimal=6 where student_name = 'VIGHNESH RAAGHAV G';

update vcet_24 set salary_decimal = 0.96 where salary_decimal = 96;

alter table `vcet_24` add column salary_in_lpa INTEGER;

update vcet_24 set salary_in_lpa = salary_decimal * 100000;

create table sorted_salary as (select `vcet_24`.`student_name`, max(`salary_in_lpa`) as sil from vcet_data.vcet_24 group by student_name order by sil desc);

create table details as (select row_number() over (order by salary_in_lpa desc) as s_no, student_name, branch, company_name, salary_in_lpa from vcet_24 order by salary_decimal desc);

SET SQL_SAFE_UPDATES = 1;create table details2 as (Select ROW_number() over (order by sil desc) as s_no, student_name, sil FROM vcet_data.sorted_salary);

