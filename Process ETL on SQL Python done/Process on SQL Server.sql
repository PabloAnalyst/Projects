--Creation of master table by joining tables
SELECT 
    df4.c1 AS df4_c1,
    df4.*,
    df3.c1 AS df3_c1,
    df3.c2,
    df3.c5,
    df3.c6
INTO Table_Master
FROM df4
INNER JOIN df3 ON df4.c1 = df3.c1;

--Creation of new tables from loaded information
SELECT DISTINCT
    c2 AS c2_new,
    c6,
    c7
INTO new_base
FROM df3;
---------------------------------------------------
SELECT DISTINCT
    c1,
    c2,
    c3 
INTO new_base2
FROM df3
WHERE c3 = 'sold';
---------------------------------------------------
-- Add new information to master table 
SELECT Table_Master.*, d5.c9
INTO Table_Master_Final
FROM Table_Master
LEFT JOIN df5 ON Table_Master.c9 = df5.c9
                     AND Table_Master.c15 = df5.c15;
select * from Table_Master


--Reduce table information size
SELECT DISTINCT *
INTO temp  
FROM Table_Master_Final;
DROP TABLE Table_Master_Final;
EXEC sp_rename 'temp', 'Table_Master_Final;
