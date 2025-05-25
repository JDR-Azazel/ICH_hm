#1. Подключаемся к базе данных northwind
use northwind;


#1. Выбираем все строки из таблицы suplier 
SELECT 
    *
FROM
    suppliers;


#2. Выбираем все строки из таблицы suplier где в столбце company содержит Supplier A
SELECT 
    *
FROM
    suppliers
WHERE
    company = 'Supplier A';


#3. Выбираем все строки из таблицы purchase_orders
SELECT 
    *
FROM
    purchase_orders;


#4. Выбираем все строки из таблицы purchase_orders где в supplier_id равен 2
SELECT 
    *
FROM
    purchase_orders
WHERE
    supplier_id = 2;


#5. Выбираем столбцы supplier_id и shipping_fee из таблицы purchase_orders где created_by равен 1 и supplier_id 5
SELECT 
    supplier_id, shipping_fee
FROM
    purchase_orders
WHERE
    created_by = 1 AND supplier_id = 5;
# select * from purchase_orders; # проверка таблицы
# Обьяснения, условия не удовлетворяется нет совпадений где одновременно created_by = 1 и supplier_id = 5 
# по этой причине запрос выдает только название строк без данных


#6. Выбираем столбцы last_name и first_name из таблицы employees 
# где столбец address содержит 123 2nd Avenue или 123 8th Avenue
SELECT 
    last_name, first_name
FROM
    employees
WHERE
    address = '123 2nd Avenue'
        OR address = '123 8th Avenue';


#6. Выбираем столбец last_name и first_name из таблицы employees 
# где в строке address присуствуют значения 123 2nd Avenue и 123 8th Avenue
SELECT 
    last_name, first_name
FROM
    employees
WHERE
    address IN ('123 2nd Avenue' , '123 8th Avenue');


#7. Выбираем строку first_name из таблици employees где last_name соответвует шаблону 
# (_%p%_) определяющему что буква p должна быть по середине и по краям должен быть обьязательно один символ
SELECT 
    first_name
FROM
    employees
WHERE
    last_name LIKE '_%p%_';
#select * from employees; # проверка


#8. Выбираем все строки из таблицы orders где столбец shipper_id не обладает никаим значением (значения null)
SELECT 
    *
FROM
    orders
WHERE
    shipper_id IS NULL;

