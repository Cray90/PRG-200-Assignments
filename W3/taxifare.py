# Taxi Fare Calculator

trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

trip_number = 1

for trip in trips:

    distance = trip["distance"]
    hour = trip["hour"]

    fare = 150

    if distance > 2:

        if distance <= 10:
            fare = fare + (distance - 2) * 35

        else:
            fare = fare + (8 * 35)
            fare = fare + (distance - 10) * 28

    # Night surcharge (10 PM to 5 AM)
    if hour >= 22 or hour < 5:
        fare = fare + (fare * 10 / 100)

    print("Trip", trip_number)
    print("Distance:", distance, "km")
    print("Hour:", hour)
    print("Fare: NPR", fare)
    print()

    trip_number = trip_number + 1