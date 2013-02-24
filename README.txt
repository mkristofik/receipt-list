Bank Statement Checklist
Michael Kristofik <kristo605@gmail.com>

SUMMARY

I'm a completeness nerd when it comes to bank statements and credit card
receipts.  I match up all my receipts to the statements when they arrive each
month.  I used to check off each line item on paper, but when most things went
paperless, I couldn't do that anymore.  Until now.

Using surprisingly little code, I was able to parse a monthly statement
(usually in *.txt or *.csv format) into an html checklist.  grep and jQuery do
the heavy lifting, and some Python glues it all together.  This project
supports three formats currently: Bank of America, American Express, and Citi
Mastercard.

REQUIREMENTS

Google Chrome browser
jQuery 1.6.1 (included)
Any flavor of Microsoft Windows with a command prompt

USAGE

amex ofx.csv
    American Express credit card statement.  Be sure to select CSV format when
    downloading your statement.
citi MM-DD-YYYY.txt
    Citi Mastercard credit card statement.  Download your statement using the
    "custom Delimiter" option and enter a comma.
money eStmt_MM_DD_YYYY.txt
    Bank of America bank statement.  PDF format statements are available on
    the Statements & Documents tab of each account in Online Banking.

LICENSE

Copyright Michael Kristofik 2011-2013.
Distributed under the Boost Software License, Version 1.0.
(See accompanying file LICENSE_1_0.txt or copy at 
http://www.boost.org/LICENSE_1_0.txt)
