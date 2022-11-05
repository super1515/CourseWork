SELECT *
	FROM departures JOIN flight USING(f_id)
		WHERE flightNumber LIKE '$number%';
