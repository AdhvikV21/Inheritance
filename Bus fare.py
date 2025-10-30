class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        
        final_fare = base_fare * 1.10
        return final_fare

bus_ride = Bus(seating_capacity=50)
calculated_fare = bus_ride.fare()

print(f"Bus Seating Capacity: {bus_ride.seating_capacity}")
print(f"Final Bus Fare: INR {calculated_fare}")