import requests
from lxml import etree

# 用户输入书名去获取本书章节





# 发送请求
url = 'https://www.quanben.io/n/guimizhizhu/1.html'
a = 0
while True:
    a += 1

    # 模仿用户数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
    }
    # 获取响应
    resp = requests.get(url, headers=headers)
    # 编码，确定响应内容的编码格式，可以获取中文
    resp.encoding = 'utf-8'

    e = etree.HTML(resp.text)
    title = e.xpath('//h1/text()')[0]
    info = '\n'.join(e.xpath("//div[@id='content']/p/text()"))
    try:
        url = f'''https://www.quanben.io{e.xpath("//span//a[text()='下一页']/@href")[0]}'''
    except IndexError:
        print('下载完成')
        break

    with open('Novel_get/诡秘之主.txt','a',encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')
    
    print(f'正在下载第{title}')


        
