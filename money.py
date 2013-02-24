#          Copyright Michael Kristofik 2011-2013.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

""" Parser for a Bank of America PDF statement. """

import checklist
import fileinput
import re

items = []
firstDate = None
lastDate = ""

def extractDate(buf):
    global firstDate, lastDate
    dt = buf[-6:-1]

    # Get the range of dates. Interest is always applied on the last line, so
    # the most recently read line will have the last date.
    if firstDate is None:
        firstDate = dt
    lastDate = dt

    return dt


for line in (i.strip() for i in fileinput.input()):
    start = line.find('Beginning Balance')
    if start == -1:
        continue

    curItem = checklist.Item()
    buf = ''
    state = 0
    for c in line[start:]:
        # Build a state machine.  Walk until we find a date.  A date starts a
        # record.  After a date we expect whitespace, then a dollar amount,
        # then more whitespace.  The first alpha character after that starts
        # the description.  Description continues until we find a date.
        #
        # states:
        # 0 - beginning
        # 1 - date found, looking for dollar amount
        # 2 - found amount, looking for description

        if state == 0:
            buf += c
            # if date found, start the first record
            if re.search('\d\d-\d\d ', buf):
                dt = extractDate(buf)
                curItem.fields.append(dt)
                buf = ''
                state = 1

        elif state == 1:
            if len(buf) == 0 and c.isdigit():
                buf += c
            elif not c.isspace():
                buf += c
            elif not len(buf) == 0:
                curItem.fields.insert(0, buf)
                # The floating-point parser gets tripped up by the commas in
                # dollar amounts greater than 1000.  Rather than bother with
                # locale stuff and parsing, I'm stripping them out.  I also
                # ignore the trailing + or - character.
                curItem.val = float(curItem.fields[0][:-1].replace(",", ""))
                buf = ''
                state = 2

        elif state == 2:
            if len(buf) == 0 and not c.isalpha():
                continue
            buf += c
            # if date found, start a new record
            if re.search('\d\d-\d\d ', buf):
                # save description to current record
                curItem.fields.append(buf[:-6])
                items.append(curItem)

                # start new record
                curItem = checklist.Item()
                dt = extractDate(buf)
                curItem.fields.append(dt)
                buf = ''
                state = 1

            # interest is always the last record
            elif 'Interest Earned' in buf:
                curItem.fields.append(buf)
                items.append(curItem)
                break

items.sort(key=lambda a: a.val)
checklist.generate("Bank of America", firstDate, lastDate, items)
