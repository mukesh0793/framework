pytest -s -v -m"sanity" --html=Reports\report.html TestCases/test_login.py --browser chrome
pytest -s -v -m"regression" --html=Reports\report.html TestCases/test_login.py --browser chrome
