#!/usr/bin/env python

title = input("Enter your page title: ")

paragraph = input("Enter your paragraph: ")

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>{}</title>
    </head>

    <body>
        <p>{}</p>
    </body>
</html>
""".format(title, paragraph)

print(html)
