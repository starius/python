import urllib2

def get_cookies(fileobj):
    reply_headers = fileobj.info()
    cookies = reply_headers.getheaders('Set-cookie')
    cookie_strings = [params.split(';')[0] for params in cookies]
    return "; ".join(cookie_strings)

