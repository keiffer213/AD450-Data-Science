--------------------------------------------------------------------
--------------------------------------------------------------------
-- Identifying Top Exporter (1990-1994) --
WITH total_exports AS (
	SELECT country, 
	SUM("1990"+"1991"+"1992"+"1993"+"1994") AS total_export
	FROM coffee_export
	GROUP BY country
)
SELECT country,
	total_export,
	DENSE_RANK() OVER(
		ORDER BY total_export DESC
	) AS export_rank
FROM
	total_exports;



--------------------------------------------------------------------
--------------------------------------------------------------------
-- Top Coffee Producers (1999-2004) --
SELECT * FROM coffee_production;

WITH total_producers AS (
	SELECT country,
		coffee_type,
		SUM("1999_2000"+"2000_2001"+"2001_2002"+"2002_2003"+"2003_2004") AS coffee_produced
	FROM coffee_production
	GROUP BY country, coffee_type
)
SELECT country, 
	coffee_type, 
	DENSE_RANK() OVER(
		ORDER BY coffee_produced DESC
	) AS producer_rank,
	coffee_produced
FROM total_producers
LIMIT 5;


--------------------------------------------------------------------
--------------------------------------------------------------------
-- Second Highest Coffee Production by Type (1990-1994) --
SELECT * FROM coffee_production;
SELECT DISTINCT coffee_type FROM coffee_production;

WITH total_producers AS (
	SELECT country,
		coffee_type,
		SUM("1990_1991"+"1991_1992"+"1992_1993"+"1993_1994") AS coffee_produced
	FROM coffee_production
	GROUP BY country, coffee_type
),
ranked_producers AS (
	SELECT country, 
		coffee_type, 
		DENSE_RANK() OVER(
			PARTITION BY coffee_type
			ORDER BY coffee_produced DESC
		) AS producer_rank,
		coffee_produced
	FROM total_producers
)
SELECT country,
	coffee_type,
	producer_rank,
	coffee_produced
FROM ranked_producers
WHERE producer_rank = 2;


--------------------------------------------------------------------
--------------------------------------------------------------------
-- Top Five Countries in Combined Exports and Imports (1995-2000) --
SELECT * FROM coffee_import;
SELECT * FROM coffee_export;

-- USING CTE METHOD --
WITH total_imp AS(
	SELECT country,
	SUM("1995"+"1996"+"1997"+"1998"+"1999"+"2000") AS total_import_1995_2000
	FROM coffee_import
	GROUP BY country
),
total_exp AS (
	SELECT country,
		SUM("1995"+"1996"+"1997"+"1998"+"1999"+"2000") AS total_export_1995_2000
	FROM coffee_export
	GROUP BY country
)
SELECT COALESCE(total_imp.country,total_exp.country) AS country,
	COALESCE(total_imp.total_import_1995_2000,0) AS total_import,
	COALESCE(total_exp.total_export_1995_2000,0) AS total_export,
	COALESCE(total_exp.total_export_1995_2000,0) + COALESCE(total_imp.total_import_1995_2000,0)AS total_combined
FROM total_imp
FULL JOIN total_exp
	ON total_imp.country = total_exp.country
ORDER BY total_combined DESC
LIMIT 5;



-- USING UNION METHOD --
SELECT country,
	SUM(total_import_1995_2000) AS total_import,
	SUM(total_export_1995_2000) AS total_export,
	SUM(total_import_1995_2000 + total_export_1995_2000) AS total_combined
FROM (
	SELECT country,
		SUM("1995"+"1996"+"1997"+"1998"+"1999"+"2000") AS total_import_1995_2000,
		0 AS total_export_1995_2000
	FROM coffee_import
	GROUP BY country
	UNION ALL
	SELECT country,
		'0' AS total_import_1995_2000,
		SUM("1995"+"1996"+"1997"+"1998"+"1999"+"2000") AS total_export_1995_2000
	FROM coffee_export
	GROUP BY country
) as combined_data
GROUP BY country
ORDER BY total_combined DESC
LIMIT 5;



--------------------------------------------------------------------
--------------------------------------------------------------------
-- Import Analysis with Country of Origin --
SELECT * FROM coffee_importers_consumption;








