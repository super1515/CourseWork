SELECT *
	FROM ticket
		WHERE saleDate BETWEEN DATE_SUB(CURDATE(), INTERVAL $num DAY) AND CURDATE();
