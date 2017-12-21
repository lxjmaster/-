# --*--coding:utf-8--*--

__AUTHOR__ = "Master_LXJ"
__DOC__ = "The dream more than endlessly!"

from urllib import request

try:
    r = request.urlopen("http://www.baidu.com")
    rs = r.read().decode("utf-8")
except Exception:
    rs = r.read().decode("gbk")

print(rs)