from FileIO import xlwork,txtwork
from settings import TEXTFILE,BASEHEADERS
from Headers import Cookies
from Proxies import Proxies
from utils import set_url
from Spider import Spider
from Parser import HtmlParser
from Verify import verify
import os
from random import randint

proxieser = Proxies("api")

if os.path.exists(TEXTFILE):
    txt = txtwork(TEXTFILE)
    dt = txt.file_to_list()
if not os.path.exists(TEXTFILE):
    wb = xlwork("公司名称.xlsx")
    dt = wb.file_to_list(TEXTFILE)

host = "http://www.qichacha.com/search?key="

def run(key):
    url = set_url(host,key)
    cookie = Cookies()
    spider = Spider(url)
    html = spider.spider(BASEHEADERS)
    if not verify(html):
        a = cookie.cookie_str(["acw_tc","PHPSESSID"])
        BASEHEADERS["Cookie"] = BASEHEADERS["Cookie"]+a
        proxieser.proxies()
        print(BASEHEADERS)
        html = spider.spider(BASEHEADERS)
    parser = HtmlParser(html)
    data = parser.parser("fund")

    print(data)
if __name__ == '__main__':
    for k in dt:
        run(k)
        time.sleep(randint(1,5))

