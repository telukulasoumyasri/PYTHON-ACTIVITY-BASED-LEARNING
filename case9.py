capacity = 50
passengers = 0

n = int(input("Enter number of stops: "))

for i in range(n):
    boarding = int(input("Enter boarding passengers: "))
    leaving = int(input("Enter leaving passengers: "))

    passengers = passengers + boarding - leaving

    if passengers > capacity:
        print("Over Capacity")
    else:
        print("Available Seats:", capacity - passengers)