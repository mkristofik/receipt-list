@echo off
python citi.py %1 > money.html
chrome.exe file:///%cd%/money.html
