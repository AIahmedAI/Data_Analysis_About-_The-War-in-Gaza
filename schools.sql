SELECT *,
COUNT(*) Over(partition by القطاع_المالك) AS NUM_ROWS,
COUNT(القطاع_المالك) over () AS NUM_القطاع_المالك,
COUNT(المحافظة) over () AS NUM_المحافظه,
COUNT(المرحلة) over () AS NUM_المرحله,
COUNT(عدد_الشهداء_من_الطلبة_لكل_مدرسة) over () AS عدد_الشهداء_من_الطلبة_لكل_مدرسه,
COUNT(عدد_الشهداء_من_معلمين_المدارس) over () AS عدد_الشهداء_من_معلمين_المدارس,
COUNT(التصنيف) over () AS التصنيف 
FROM SCHOOL;

update school
Set التصنيف='school'
where التصنيف IS NULL

ALTER TABLE school
ALTER COLUMN التصنيف NVARCHAR(100);
SELECT *
FROM SCHOOL