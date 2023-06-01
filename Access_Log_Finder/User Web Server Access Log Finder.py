"""
Find user ids in the web server access log that do not conform to the 'slash-tilde' pattern

 Author: Matthew Judson (mrj628809@gmail.com)
 Last Revised: 2/13/2023
"""

import re

fh = open('access_log.txt')
count = 0
users = {}

for log in fh:
    if re.search(r'[a-za-z]{2,}\d{2,}', log) and re.search(r'\d{2,}$', log):
        nyid, bytes = re.search(r'[a-za-z]{2,}\d{2,}', log).group(0), re.search(r'\d{2,}$', log).group(0)
        count += 1

        if nyid not in users:
            users[nyid] = int(bytes)

        else:
            users[nyid] += int(bytes)

print(f'{count} matches found (user id and end-of-line bytes\n')

for user in sorted(users, key=users.get, reverse=True):
    if users[user] > 10000000:
       print(f'{user}: {users[user]}')





