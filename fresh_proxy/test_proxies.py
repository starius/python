import urllib2
import sys
import optparse


# get options
parser = optparse.OptionParser()
parser.add_option('-p', help='file with proxies', dest='proxies')
parser.add_option('-t', dest='timeout')
parser.add_option('-u', dest='url')
options, args = parser.parse_args()

timeout = int(options.timeout)
url = options.url

for proxy in [str.strip() for str in open(options.proxies)]:
    if not proxy:
        continue
    req = urllib2.Request(url)
    req.set_proxy(proxy, "http");
    
    try:
        r = urllib2.urlopen(req, timeout = timeout)
        if r.read():
            print proxy
    except:
        continue
