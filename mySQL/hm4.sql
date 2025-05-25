# 1 Подключитесь к своей базе данных созданной на уроке

use 210225_Boiko;

# 2 Создайте таблицу, которая отражает погоду в Вашем городе за последние 5 дней и включает следующее 
# столбцы Id - первичный ключ, заполняется автоматически
# Дата - не может быть пропуском
# Дневная температура - целое число, принимает значения от -30 до 30
# Ночная температура - целое число, принимает значения от -30 до 30
# Скорость ветра - подумайте какой тип данных и ограничения необходимы для этого столбца

CREATE TABLE Weather (
    dayID INT AUTO_INCREMENT PRIMARY KEY,
    check_date date NOT NULL,
    daytime_c int check (daytime_c between -30 and 30),
    nightime_c int check (nightime_c between -30 and 30),
    wind_m_s decimal(3, 1) 
 );

# 3 Заполните таблицу 5 строками - за последние 5 дней 

INSERT INTO Weather (check_date, daytime_c, nightime_c, wind_m_s) 
VALUES
	('2025-03-24', 11, 4, 1),
	('2025-03-25', 10, 3, 0.5),
	('2025-03-26', 13, 8, 51.3),
	('2025-03-27', 15, 9, 41.3),
	('2025-03-28' , 16, 5, 10.3);

SELECT 
    *
FROM
    v_Weather;

# 4 Увеличьте значения ночной температуры на градус если скорость ветра не превышала 3 м/с

UPDATE Weather 
SET 
    nightime_c = nightime_c + 1
WHERE
    wind_m_s <= 3;

# 5 На основе полученной таблицы создайте представление в своей базе данных - включите все строки Вашей таблицы и дополнительно рассчитанные столбцы
# Средняя суточная температура - среднее арифметическое между ночной и дневной температурами
# Столбец на основе скорости ветра - если скорость ветра не превышала 2 м/с то значение ‘штиль’,
# от 2 включительно до 5 - ‘умеренный ветер’, в остальных случаях - ‘сильный ветер’

# Коментрий: среднее арифметическое в питоне решал бы при помощи цикла тут циклы еще не учили поэтому составил запрос с учетом 5 столбцов

CREATE VIEW v_Weather AS
SELECT 
    *, 
    (daytime_c + nightime_c) / 2 AS difference_c,
    ( (SELECT daytime_c FROM Weather WHERE dayID = 1) + 
      (SELECT daytime_c FROM Weather WHERE dayID = 2) + 
      (SELECT daytime_c FROM Weather WHERE dayID = 3) + 
      (SELECT daytime_c FROM Weather WHERE dayID = 4) + 
      (SELECT daytime_c FROM Weather WHERE dayID = 5) ) / 5 AS aritmetik_daytime_c_diff,
    CASE
        WHEN wind_m_s < 2 THEN 'штиль'
        WHEN wind_m_s >= 2 AND wind_m_s < 5 THEN 'умеренный ветер'
        ELSE 'сильный ветер'
    END AS wind_classification  
FROM 
    Weather;

# 6 Отформатируйте стиль написания запросов
# 7 Сохраните запросы в виде файла с расширением .sql и загрузите на платформу