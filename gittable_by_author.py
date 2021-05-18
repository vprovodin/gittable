import os
import re

f = open('/Users/vprovodin/PycharmProjects/gittable/authors.txt', 'r')
of = open('/Users/vprovodin/PycharmProjects/gittable/gtable.txt', 'w')
of.write('|Author|SHA|Description|Target|Status|\n')
#of.write('|---|---|----|---|---|\n')
for l in f:
    email = re.search(r'^.*<(.*)>', l).group(1)
    stream = os.popen('git log --pretty=format:\"%h %s %cd\" --author=' + email + ' master | grep -v \"updated JTreg exclude list\"')
    first = True
    for c in stream.readlines():
        res = re.search(r'^(\w*) (.*)', c)
        if first:
            s = '|' + email + '|' + res.group(1) + '|' + res.group(2) + '| master14 | |\n'
            first = False
        else:
            s = '| |' + res.group(1) + '|' + res.group(2) + '| master14 | |\n'
        of.write(s)
