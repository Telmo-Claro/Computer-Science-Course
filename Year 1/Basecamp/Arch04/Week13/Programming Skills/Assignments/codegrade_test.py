import carparking as cp
from datetime import datetime, timedelta

cpm = cp.CarParkingMachine(id="North",capacity=2, hourly_rate=4.0)
cpm.check_in("BB-494-H")
cpm.check_in("HH-494-B")

print(cpm.parked_cars)


cpm = cp.CarParkingMachine(id="South",capacity=2, hourly_rate=4.0)
cpm.check_in("BB-495-H")
cpm.check_in("HH-495-B", datetime.now() - timedelta(hours=2))

print(cpm.hourly_rate)
print(cpm.check_out("BB-495-H"))