# Вывести названия продуктов таблица products, включая количество заказанных единиц quantity для каждого продукта таблица order_details.
# Решить задачу с помощью cte и подзапроса.
use northwind;

# CTE
WITH CTE AS (
    SELECT 
        product_id, 
        SUM(quantity) AS sum_quantity
    FROM 
        order_details
    GROUP BY 
        product_id
)

SELECT 
    p.id, 
    p.product_name, 
    (
        SELECT 
            CTE.sum_quantity 
        FROM 
            CTE 
        WHERE 
            p.id = CTE.product_id
    ) AS order_quantity
FROM 
    products AS p;


# SUB
SELECT 
    p.id,
    p.product_name,
    (SELECT 
            SUM(od.quantity)
        FROM
            order_details AS od
        WHERE
            p.id = od.product_id) AS order_quantity
FROM
    products AS p;

# Найти все заказы таблица orders, сделанные после даты самого первого заказа клиента Lee таблица customers.

SELECT 
    *
FROM
    orders
WHERE
    order_date > (SELECT 
            MIN(o.order_date)
        FROM
            orders AS o
                JOIN
            customers AS c ON o.customer_id = c.id
        WHERE
            c.last_name = 'Lee');

select last_name from customers where last_name = "Lee";

select * from customers;
select * from orders;
select * from products;

# Найти все продукты таблицы  products c максимальным target_level

SELECT 
    *
FROM
    products
WHERE
    target_level = (SELECT 
            MAX(target_level)
        FROM
            products);