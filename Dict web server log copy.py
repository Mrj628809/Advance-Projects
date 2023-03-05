"""
 Build a dict from a web server log that sums up web server usage by user id

 Author: Matthew Judson (mrj628809@gmail.com)
 Last Revised: 2/9/2023
"""

import re

fh = open('access_log.txt')
count = 0
users = {}

for log in fh:
    id_match = re.search(r'/~(([a-zA-Z]{2,})(\d+))', log)
    bytes_match = re.search(r'(\d+)$', log)

    if id_match and bytes_match:
        nyid, bytes = id_match.group(1), int(bytes_match.group(1))

        count += 1

        if nyid not in users:
            users[nyid] = bytes
        else:
            users[nyid] += bytes

print(f'{count} matches found (both user id and end-of-line bytes found on the line)\n')

for user in sorted(users, key=users.get, reverse=True):
    if users[user] > 10000000:
        print(f'{user}: {users[user]}')





