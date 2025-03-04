SELECT country, "1990_1991", "1991_1992"
FROM coffee_production;


WITH cum_prod AS (
   SELECT
	   P.coffee_type, 
	   P.country, 
	   SUM(P."1990_1991" + P."1991_1992" + P."1993_1994" + P."1994_1995") as cum_volume
	FROM coffee_production AS P
	GROUP BY P.coffee_type, P.country
   ), 
   rank_prod AS (
	SELECT coffee_type, country,
		RANK() OVER (PARTITION BY coffee_type ORDER BY cum_prod) AS rank
		FROM cum_prod
) SELECT * FROM rank_prod WHERE rank = '2'