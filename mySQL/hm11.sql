# 1. Функция для расчета площади круга
use 210225_Boiko;
DELIMITER //

CREATE FUNCTION square_calculator(n decimal(10, 5))
RETURNS DECIMAL(20, 5)
DETERMINISTIC
BEGIN
	RETURN 3.14159 * POW(n, 2);
END//
DELIMITER ;

select square_calculator(10.20);
SHOW CREATE FUNCTION square_calculator;

# 2. Функция для расчета гипотенузы треугольника

DELIMITER //

CREATE FUNCTION hypotenuse_calculator(a decimal(10,5), b decimal(10,5))
RETURNS DECIMAL(20,5)
DETERMINISTIC
BEGIN
    RETURN SQRT(POW(a, 2) + POW(b, 2));
END//

DELIMITER ;

select hypotenuse_calculator(10, 20);