def test_parking_fee():
    garage = CarParkingMachine("W")
    # Assert that parking time 2h10m, gives correct parking fee
    garage.check_in("Ad", datetime.now() - timedelta(hours=2, seconds=10))
    assert garage.get_parking_fee("Ad") == 7.5