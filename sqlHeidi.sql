SELECT ta_stock.id, symbol, company, exchange, stockID, close, date
  FROM ta_stockprice JOIN ta_stock ON ta_stockprice.stockID = ta_stock.id
  GROUP BY ta_stock.id
  HAVING COUNT(*) > 50 AND stockID = 8648
  ORDER by DATE DESC

SELECT ta_stock.id, symbol, company, exchange, stockID, MIN(close), date
  FROM ta_stockprice JOIN ta_stock ON ta_stock.id = ta_stockprice.stockID
  GROUP BY ta_stock.id
  HAVING COUNT(*) > 50
  ORDER by DATE DESC

SELECT * FROM (
	SELECT ta_stock.id, symbol, company, exchange, stockID, MIN(close), date
	  FROM ta_stockprice JOIN ta_stock ON ta_stock.id = ta_stockprice.stockID
	  GROUP BY ta_stock.id
	  HAVING COUNT(*) > 50
	  ORDER by DATE DESC
) sub WHERE DATE > "2021-06-30"
  
SELECT * FROM ta_stockprice 
WHERE stockid = 8648
ORDER BY close DESC



SELECT stockID, DATE, close, symbol
  FROM ta_stockprice JOIN ta_stock ON ta_stock.id = ta_stockprice.stockID
WHERE stockid = 8648
ORDER BY close DESC



SELECT * FROM ta_stock
ORDER BY symbol

SELECT stockID, symbol,  COUNT(*)
FROM ta_stockprice JOIN ta_stock ON ta_stock.id = ta_stockprice.stockID
GROUP BY stockID
HAVING COUNT(*) > 50
ORDER BY COUNT(*) ASC, symbol ASC