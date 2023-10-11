# Written by Quinn Black
# August 17, 2023

import re

# read text body of log into variable

with open('sys_log.txt','r') as file:
    sLogText = file.read()

''' 

Regex case examples to test for:
 case #1 - service:"80" 
 case #2 - s_port:"60641"
 case #3 - Port: 19778
 case #4 - port 11332

NOTE: these cases are tailored specifically for the log example provided. In a
more realistic work scenario, a variety of other cases would need to be tested
to ensure accuracy

'''

pattern1 = r'(?i)(?:port|service)[:"\s]*(\d+)'

matches = re.findall(pattern1, sLogText, re.DOTALL)

print(matches)


