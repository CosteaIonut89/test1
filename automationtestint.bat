@echo off 
pytest -p no:logging -v -s --html=report.html --capture=tee-sys --self-contained-html -rx --verbose --maxfail=16 "D:/Python Projects/StackField/testCases/test_basic.py"
pytest -p no:logging -v -s --html=report_sprint.html --capture=tee-sys --self-contained-html -rx --verbose --maxfail=16 "D:/Python Projects/StackField/testCases/test_basic_sprint.py"
"C:\Program Files\Python310\python.exe" "D:\Python Projects\StackField\sending_email.py"
exit

