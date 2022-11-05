SELECT departurePoint, arrivalPoint, COUNT(cost), SUM(cost)
	FROM (ticket JOIN departures USING(d_id)) JOIN flight USING(f_id)
    WHERE saleDate BETWEEN '$date_in' AND '$date_out'
	GROUP BY f_id;