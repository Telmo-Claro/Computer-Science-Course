from carparking import *
from datetime import datetime, timedelta


# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    garage = CarParkingMachine()
    assert garage.check_in("Ad") == True


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    garage = CarParkingMachine(1)
    garage.check_in("Ad")
    assert garage.check_in("Aq") == False


# Test for checking the correct parking fees
def test_parking_fee():
    garage = CarParkingMachine()
    # Assert that parking time 2h10m, gives correct parking fee
    garage.check_in("Ad", datetime.now() - timedelta(hours=2, seconds=10))
    assert garage.get_parking_fee("Ad") == 7.5
    # Assert that parking time 24h, gives correct parking fee
    garage.check_in("Ab", datetime.now() - timedelta(hours=24))
    assert garage.get_parking_fee("Ab") == 60.0
    # Assert that parking time 30h == 24h max, gives correct parking fee
    garage.check_in("Ac", datetime.now() - timedelta(hours=30))
    assert garage.get_parking_fee("Ac") == 60.0


# Test for validating check-out behavior
def test_check_out():
    # Assert that {license_plate} is in parked_cars
    garage = CarParkingMachine()
    garage.check_in("Ad")
    assert "Ad" in garage.parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    garage = CarParkingMachine()
    garage.check_in("Ab", datetime.now())
    assert garage.check_out("Ab") == 2.5
    # Assert that {license_plate} is no longer in parked_cars
    garage = CarParkingMachine()
    garage.check_in("Ac")
    garage.check_out("Ac")
    assert "Ac" not in garage.parked_cars
test_check_out()
