from settings import PROXIES_POOL,PROXIES_API
from random import choice
from urllib import request


class Proxies(object):
    def __init__(self,method):
        self.method = method
        self.proxie = []
        self.pool = []

    def manual(self):
        self.proxies = choice(PROXIES_POOL)

        return self.proxies

    def api_get_proxies(self):
        requester = request.urlopen(PROXIES_API)
        response = requester.read()
        self.proxies_pool = str(response).split()

        return self.proxies_pool

    def proxies(self):
        if self.method == "manual":
            self.proxie = self.manual()
        if self.method == "api":
            self.proxie = self.get_proxies()
        proxies_handler = request.ProxyHandler({"http":self.proxie[-1],"https":self.proxie[-1]})
        opener = request.build_opener(proxies_handler)
        request.install_opener(opener)
        self.pool.pop()


    def get_proxies(self):
        if len(self.pool) == 0:
            self.pool = self.api_get_proxies()
        proxies = self.pool

        return proxies