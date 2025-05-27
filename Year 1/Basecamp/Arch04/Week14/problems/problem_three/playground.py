from result import Result
from resultsmanager import ResultsManager

rm = ResultsManager()
rm.create_tables()

print(rm.add_result(Result(1, 1, 40, "2023-06-12")))
print(rm.add_result(Result(1, 1, 70, "2023-06-12")))