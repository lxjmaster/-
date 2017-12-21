from lxml import etree
from settings import RULE


class HtmlParser(object):
    def __init__(self,response):
        self.response = response

    def parser(self,data_name,rule_name="Xpath"):
        tree = etree.HTML(self.response)
        data = tree.xpath("/html/body/div[2]/div/div[1]/div[2]/section/table/tbody/tr[1]/td[2]/p[1]/span[1]")
        if not rule_name:
            pass    #暂空

        print(data)

        return data