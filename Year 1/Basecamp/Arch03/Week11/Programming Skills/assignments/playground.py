import sqlite3
import os
from datetime import datetime
import math
import sqlite3
import sys

id = input("ID: ")
db_conn = sqlite3.connect('carparkingmachine.db')
fetched_car = db_conn.execute("SELECT * FROM parkings WHERE id=?", [id]).fetchone()
print(fetched_car)