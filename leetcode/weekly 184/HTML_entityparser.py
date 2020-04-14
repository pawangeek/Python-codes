# HTML Entity Parser
# https://leetcode.com/contest/weekly-contest-184/problems/html-entity-parser/

text = "&amp; is an HTML entity but &ambassador; is not."
r = {"&quot;": '"',"&apos;": "'","&amp;": "&","&gt;": ">","&lt;": "<","&frasl;": "/",}

for k, v in r.items():
    text = text.replace(k, v)
    
print(text)