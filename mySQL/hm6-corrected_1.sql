# 1 Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders и соответствующие 
# им столбцы из таблицы purchase_orders В таблице purchase_orders created_by соответствует employee_id
use northwind;

SELECT 
    id, employee_id
FROM
    orders 
UNION SELECT 
    id, created_by
FROM
    purchase_orders;

select * from purchase_orders;

# 2 Из предыдущего запроса удалите записи там где employee_id не имеет значения. Добавьте дополнительный столбец
#  со сведениями из какой таблицы была взята запись

SELECT 
    id, employee_id, 'orders' AS table_
FROM
    orders
WHERE
    employee_id IS NOT NULL 
UNION SELECT 
    id, created_by, 'purchase_orders' AS table_
FROM
    purchase_orders
WHERE
    created_by IS NOT NULL;

# 3 Выведите все столбцы таблицы order_details а также дополнительный столбец payment_method из таблицы 
# purchase_orders Оставьте только заказы для которых известен payment_method

SELECT 
    *, purchase_orders.payment_method
FROM
    order_details
        JOIN
    products ON order_details.product_id = products.id
        JOIN
    purchase_order_details ON products.id = purchase_order_details.product_id
        JOIN
    purchase_orders ON purchase_order_details.purchase_order_id = purchase_orders.id
WHERE
    payment_method IS NOT NULL;

select * from invoices;

# 4 Выведите заказы orders и фамилии клиентов customers для тех заказов по которым были инвойсы таблица invoices

SELECT 
    o.*, c.last_name
FROM
    orders as o
        JOIN
    customers as c ON o.customer_id = c.id
        JOIN
    invoices as i ON o.id = i.order_id;

# 5 Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса
# ID уникальны можно по ним сортирвать 

SELECT 
	c.id,
    c.last_name,
    COUNT(i.id) AS invoices_per_customer
FROM
    orders as o
        JOIN
    customers as c ON o.customer_id = c.id
        JOIN
    invoices as i ON o.id = i.order_id
GROUP BY 1, 2;

select * from customers;

# Но ID может отвечать за строку а не пользователя поэтому также можно отсортирвоать по имени и фамилии
# шанс что будут два разных человека в одной компании с одинаковым именем и фамилией крайне мал 

SELECT 
    concat(c.last_name, ' ', c.first_name) as full_name,
    COUNT(i.id) AS invoices_per_customer
FROM
    orders as o
        JOIN
    customers as c ON o.customer_id = c.id
        JOIN
    invoices as i ON o.id = i.order_id
GROUP BY full_name;

select * from customers;