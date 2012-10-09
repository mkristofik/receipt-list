rem          Copyright Michael Kristofik 2011-2012.
rem Distributed under the Boost Software License, Version 1.0.
rem    (See accompanying file LICENSE_1_0.txt or copy at
rem          http://www.boost.org/LICENSE_1_0.txt)

@echo off
python citi.py %1 > money.html
chrome.exe file:///%cd%/money.html
del /p %1
