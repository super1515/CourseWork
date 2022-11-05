select
    departureDate,
    departureTime,
    arrivalDate,
    arrivalTime,
    flightNumber,
    departurePoint,
    arrivalPoint,
    baseCost
from departures JOIN flight USING(f_id)