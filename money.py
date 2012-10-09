#          Copyright Michael Kristofik 2011-2012.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

""" Parser for a Bank of America statement. """

import checklist
import fileinput

items = []
firstDate = None
lastDate = ""

for line in (i.strip() for i in fileinput.input()):
    i = checklist.Item()
    i.fields = line.split()

    # Get the range of dates. Interest is always applied on the last line, so
    # the most recently read line will have the last date.
    if firstDate is None:
        firstDate = i.fields[0]
    lastDate = i.fields[0]

    # The floating-point parser gets tripped up by the commas in dollar amounts
    # greater than 1000.  Rather than bother with locale stuff and parsing, I'm
    # stripping them out.  I also ignore the trailing + or - character.
    i.val = float(i.fields[1][:-1].replace(",", ""))

    # Make the dollar amount appear first.
    i.fields[0], i.fields[1] = i.fields[1], i.fields[0]
    # Don't need to see total balance.
    del i.fields[2]

    items.append(i)

items.sort(key=lambda a: a.val)
checklist.generate("Bank of America", firstDate, lastDate, items)
