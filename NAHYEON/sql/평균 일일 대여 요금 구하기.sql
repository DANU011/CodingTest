SELECT ROUND(AVG(DAILY_FEE), 0) AS 'AVERAGE_FEE'
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';

-- ROUND(값, 자릿수)
-- 자릿수를 넣지 않을 경우에는 소수를 모두 반올림 
-- 자리수를 넣을 경우에는 자리수 위치까지 반올림 수행