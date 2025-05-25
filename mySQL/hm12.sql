use 210225_Boiko;

CREATE TABLE employees_data(id INT AUTO_INCREMENT PRIMARY KEY, departament_id INT, age INT, salary DECIMAL(6, 2));

INSERT INTO employees_data(departament_id, age, salary) VALUES (666, 24, 1610.12), (777, 41, 7021.56), (888, 22, 5210.00), (999, 25, 4709.00);

DELIMITER //

# 1 Вывести id департамента , в котором работает сотрудник, в зависимости от Id сотрудника

CREATE PROCEDURE get_departament_id(IN emp_id INT)
BEGIN
	SELECT departament_id FROM employees_data WHERE id = emp_id;
END //

# 2 Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника (IN-параметр) и возвращает его возраст через OUT-параметр.

CREATE PROCEDURE get_employee_age(IN emp_id INT, OUT emp_age INT)
BEGIN 
	SELECT age INTO emp_age FROM employees_data WHERE id = emp_id;
END //
	
# 3 Создайте хранимую процедуру increase_salary, которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.

CREATE PROCEDURE increase_salary(INOUT salary DECIMAL(6, 2))
BEGIN
	SET salary = salary * 0.90;
END //

DELIMITER ;

CALL get_departament_id(1); # 1

SET @age = 0;
CALL get_employee_age (1, @age); # 2
SELECT @age as employee_age;

SET @test_salary = 2900;
CALL increase_salary(@test_salary); # 3
SELECT @test_salary as decresed_salary;