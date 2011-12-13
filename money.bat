@echo off
grep -P "\.\d\d[+|-]" %1 | python money.py - > money.html
chrome.exe file:///%cd%/money.html
del /p %1
