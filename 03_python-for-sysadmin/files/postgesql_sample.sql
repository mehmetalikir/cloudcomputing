SELECT * FROM employees;

SELECT gender FROM employees WHERE gender = 'Female';

SELECT * FROM employees WHERE email LIKE '%tt%';

SELECT * FROM EMPLOYEES WHERE first_name NOT LIKE '%a%' AND id BETWEEN 200 AND 220;

SELECT * FROM EMPLOYEES WHERE id>900 AND (last_name LIKE '%tt%' OR last_name LIKE '%ll%');

SELECT last_name FROM employees WHERE employees.email LIKE '%ll%' AND id <= 100;