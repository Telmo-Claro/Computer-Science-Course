import carparking as cp
from datetime import datetime, timedelta

cpm = cp.CarParkingMachine(capacity=2, hourly_rate=4.0)
cpm.check_in("BB-494-H")
cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))

print(cpm.get_parking_fee("HH-494-B"))
