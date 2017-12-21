from urllib import request
from http import cookiejar
from settings import BASEHEADERS


headers = {
        "Host":"www.qichacha.com",
        "Referer":"http://www.qichacha.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
}

class Cookies(object):
    def __init__(self):
        self.url = "http://"+BASEHEADERS["Host"]
        self.cj = cookiejar.LWPCookieJar()
        cookie_support = request.HTTPCookieProcessor(self.cj)
        opener = request.build_opener(cookie_support,request.HTTPHandler)
        request.install_opener(opener)
        requester = request.Request(self.url,headers=headers)
        request.urlopen(requester)


    def get_cookies_dict(self):
        lwp = self.cj._cookies
        lwp_dict = lwp[BASEHEADERS["Host"]]
        
        return lwp_dict
        
    def get_cookie(self,name):
        cook_list = []
        lwp_dict = self.get_cookies_dict()
        cookie_dict = lwp_dict["/"]
        for n in name:
            cookie = cookie_dict[n]
            cook_list.append(cookie)

        return cook_list



    def cookie_str(self,names):
        cookie = self.get_cookie(names)
        s = "{name}={values}".format(name=cookie[0].name,values=cookie[0].value) + "; " + "{name}={values}".format(name=cookie[1].name,values=cookie[1].value) + "; "

        print(s)
        return s