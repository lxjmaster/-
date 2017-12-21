from urllib import request


class Spider(object):

    def spider(self,url,headers=None):
        try:
            requester = request.Request(url,headers=headers)
            opener = request.urlopen(requester)
            response =opener.read()
        except Exception as e:
            print(e)

        return response