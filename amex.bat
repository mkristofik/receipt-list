@echo off
python amex.py %1 > money.html
chrome.exe file:///%cd%/money.html
