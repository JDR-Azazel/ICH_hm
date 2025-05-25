# 1. Таблица purchase_order_details. Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost
use northwind;

select * from purchase_order_details;

SELECT 
    purchase_order_id,
    MIN(unit_cost) OVER (partition BY purchase_order_id) AS min_cost,
    MAX(unit_cost) OVER (PARTITION BY purchase_order_id) AS max_cost,
    AVG(unit_cost) OVER (PARTITION BY purchase_order_id) AS avg_cost
FROM 
    purchase_order_details;

# 2  Оставьте только уникальные строки из предыдущего запроса

SELECT DISTINCT
    purchase_order_id,
    MIN(unit_cost) OVER (partition BY purchase_order_id) AS min_cost,
    MAX(unit_cost) OVER (PARTITION BY purchase_order_id) AS max_cost,
    AVG(unit_cost) OVER (PARTITION BY purchase_order_id) AS avg_cost
FROM 
    purchase_order_details;

# 3 Посчитайте стоимость продукта в заказе как quantity*unit_cost Выведите суммарную стоимость
# продуктов с помощью оконной функции Сделайте то же самое с помощью GROUP BY

# OVER
SELECT 
    product_id, 
    quantity * unit_cost AS product_price, 
    SUM(quantity * unit_cost) OVER (PARTITION BY product_id) AS total_price
FROM 
    purchase_order_details;

# GROUP BY
SELECT 
    product_id, SUM(quantity * unit_cost) total_price
FROM
    purchase_order_details
GROUP BY product_id;

# 4 Посчитайте количество заказов по дате получения и posted_to_inventory Если оно превышает 1 то выведите '>1' в противном случае '=1'
# Выведите purchase_order_id, date_received и вычисленный столбец

select * from purchase_order_details;

SELECT 
    purchase_order_id, 
    date_received, 
    COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory) AS order_quantity,
    CASE 
        WHEN COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory) > 1 THEN '>1'
        ELSE '=1'
    END AS status_
FROM 
    purchase_order_details;


