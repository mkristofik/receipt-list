::           Copyright Michael Kristofik 2011-2012.
::  Distributed under the Boost Software License, Version 1.0.
::     (See accompanying file LICENSE_1_0.txt or copy at
::           http://www.boost.org/LICENSE_1_0.txt)

@echo off
python amex.py %1 > money.html
chrome.exe file:///%cd%/money.html
del /p %1
