import requests
from lxml import etree


# 用户输入书名去获取本书章节

user = input('请输入书名(Book Name)：')

serch = 'https://www.quanben.io/index.php?c=book&a=search&keywords=' + user

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

res = requests.get(serch, headers=header)
res.encoding = 'utf-8'
e = etree.HTML(res.text)

booklist = '\n'.join(e.xpath("//div[@class='list2']/h3/a/span/text()"))  # 获取书名
print(booklist)

for i, book in enumerate(booklist.split('\n'),start = 1):
    print(f"{i}. {book}")

choice = input('Choice number: ')    # Choose Book Num

# 获取书名对应的url
url = f'''https://www.quanben.io{e.xpath("//div[@class='list2']/h3/a/@href")[int(choice) - 1]}1.html'''


open('1.Novel_get/诡秘之主.txt','w',encoding='utf-8').close()

# Download Novel
while True:

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



    with open('1.Novel_get/诡秘之主.txt','a',encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')
    
    print(f'正在下载第{title}')


        
