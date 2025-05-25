# 1 Посчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.

SELECT 
    AVG(unit_cost) AS average,
    SUM(unit_cost) AS summa,
    MIN(unit_cost) AS minimum,
    MAX(unit_cost) AS maximum
FROM
    purchase_order_details;

# 2 Посчитайте количество уникальных заказов purchase_order_id

SELECT 
    COUNT(DISTINCT purchase_order_id) AS uniq_orders
FROM
    purchase_order_details;

# 3 Посчитайте количество продуктов product_id в каждом заказе purchase_order_id Отсортируйте полученные данные по убыванию количества

SELECT 
    purchase_order_id, COUNT(product_id) AS prod_quntiti
FROM
    purchase_order_details
GROUP BY purchase_order_id
ORDER BY 2 DESC;

# 4 Посчитайте заказы по дате доставки date_received Считаем только те продукты, количество quantity которых больше 30

SELECT 
    date_received,
    COUNT(purchase_order_id) orders_more_30
FROM
    purchase_order_details
WHERE
    quantity > 30
GROUP BY date_received;

SELECT 
    *
FROM
    purchase_order_details;

# 5 Посчитайте суммарную стоимость заказов в каждую из дат Стоимость заказа - произведение quantity на unit_cost
use northwind;

SELECT 
    date_received, SUM(quantity * unit_cost) AS order_price
FROM
    purchase_order_details
GROUP BY date_received;

# 6 Сгруппируйте товары по unit_cost и вычислите среднее и максимальное значение quantity только для товаров где purchase_order_id не больше 100

SELECT 
    unit_cost, 
    AVG(quantity) AS average_quant, 
    MAX(quantity) AS maximum_quant
FROM purchase_order_details
WHERE purchase_order_id <= 100
GROUP BY unit_cost;

# 7 Выберите только строки где есть значения в столбце inventory_id Создайте столбец category - 
#если unit_cost > 20 то 'Expensive' в остальных случаях 'others' Посчитайте количество продуктов в каждой категории

SELECT 
    COUNT(inventory_id),
    CASE
        WHEN unit_cost > 20 THEN 'Expensive'
        ELSE 'others'
    END AS category
FROM
    purchase_order_details
WHERE
    inventory_id IS NOT NULL
GROUP BY category
;