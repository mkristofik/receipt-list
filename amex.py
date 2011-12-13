import checklist
import fileinput

items = []
firstDate = None
lastDate = ""

for line in (i.strip() for i in fileinput.input()):
    if not line:
        continue

    i = checklist.Item()
    i.fields = line.split(',')

    # Get the range of dates. The input data is sorted by date, so the most
    # recently read line will have the last date.
    if firstDate is None:
        firstDate = i.fields[0]
    lastDate = i.fields[0]

    # Remove unneeded fields.
    del i.fields[1]
    del i.fields[3:]

    i.val = float(i.fields[1])

    # Make the dollar amount appear first.
    i.fields[0], i.fields[1] = i.fields[1], i.fields[0]

    items.append(i)

items.sort(key=lambda a: a.val)
items.reverse()
checklist.generate("American Express", firstDate, lastDate, items)
