# DateAnnotation decode question
import requests
from lxml import etree
def decode(url):
    # requests to get html
    response = requests.get(url)
    html = etree.HTML(response.text)
    patterns = {}
    # Find Decoding Table
    rows = html.xpath('//table//tr')
    for row in rows[1:]: # skip row 1
        data = row.xpath("./td//text()")
        # print(data)

        x = int(data[0])
        y = int(data[2])
        char = data[1]

        # print(f"{x} {y} {char}")
        
        patterns[(x, y)] = char # {(0, 0): '█'}
       # print(patterns)
        
    max_x = max([x for x, y in patterns.keys()]) # 3
    max_y = max([y for x, y in patterns.keys()]) # 2
    
    # print(max_x, max_y)
     
    # draw pattern
    for y in range(max_y, -1, -1):
        a = ''
        for x in range(max_x + 1):
            a += patterns.get((x, y), ' ')
        print(a)



url = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'
decode(url)