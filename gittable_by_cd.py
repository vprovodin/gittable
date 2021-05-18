import os
import re

f = open('/Users/vprovodin/PycharmProjects/gittable/authors.txt', 'r')
of = open('/Users/vprovodin/PycharmProjects/gittable/gtable.txt', 'w')
of.write('Author|SHA|Commit Date|Description|Status\n')

authors = f.readlines()
f.close()

#of.write('|---|---|----|---|---|\n')
stream = os.popen('git log --pretty=format:\"%ae %h %cd %s \" --date=short master | grep -v \"updated JTreg exclude list\"')
first = True
for c in stream.readlines():
    #res = re.search(r'(\w*\.\w*\@\w*\.\w*) (\w*) (.*)', c)
    email = c.split()[0]
    res = re.search(r'^(\w*) (\d{4}\-\d{2}\-\d{2}) (.*)', c.removeprefix(email + " "))
    doprint = False
    for l in authors:
        if (l.find(email) != -1 ):
            doprint = True
    if doprint:
        s = email + '|' + res.group(1) + '|' + res.group(2) + '|' + res.group(3) + '|\n'
        print(s)
        of.write(s)
