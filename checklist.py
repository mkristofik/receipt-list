from string import Template

class Item:
    def __init__(self):
        self.val = 0.0
        self.fields = []


def printHeader(bank, firstDate, lastDate):
    s = Template("""<!DOCTYPE html>
<html>
<head>
    <title>$name Receipt Checklist</title>
</head>
<body>
    <h2>$name receipts from $fromDate to $toDate</h2>""")
    print s.substitute(name = bank, fromDate = firstDate, toDate = lastDate)


def printItems(itemList):
    for i in itemList:
        print '    <label><input type="checkbox"> ',
        print "&nbsp;&nbsp;".join(i.fields),
        print "</label><br>"


def printRest():
    print """    <script src="jquery-1.6.1.min.js"></script>
    <script>
        $(document).ready(function () {
            $("input").click(function (event) {
                var parentLabel = $(event.target).parent(),
                    isChecked = $(event.target).attr("checked");

                if (isChecked) {
                    $(parentLabel).css("textDecoration", "line-through");
                    $(parentLabel).css("color", "lightgrey");
                }
                else {
                    $(parentLabel).css("textDecoration", "none");
                    $(parentLabel).css("color", "inherit");
                }
            });
        });
    </script>
</body>
</html>"""


def generate(bank, firstDate, lastDate, itemList):
    printHeader(bank, firstDate, lastDate)
    printItems(itemList)
    printRest()
