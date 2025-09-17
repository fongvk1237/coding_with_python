import sys
import re

if len(sys.argv) != 3:
    print("none")
else :
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(keyword, text)
    
    if matches :
        print(len(matches))
    else :
        print("none")