@echo off
grep -P "\d\d-" %1 | grep " [-|+] " | python money.py - > money.html
chrome.exe file:///%cd%/money.html
del /p %1
