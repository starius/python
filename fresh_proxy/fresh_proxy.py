import urllib2
import re

pattern_ip = """(\d+.\d+.\d+.\d+)<script type="text/javascript">document.write\(":"([^\)]+)\)"""

for i in range(1, 999):
    url = 'http://nntime.com/proxy-list-%02d.htm' % i
    try:
        html = urllib2.urlopen(url).read()
        
        #s=9;m=6;q=5;h=0;z=1;u=2;w=3;l=4;n=8;v=7;
        letters = re.search("((\w)=(\d);){10}", html)
        letters = re.finditer("(\w)=(\d);", letters.group())
        translate = []
        for letter, number in [x.groups() for x in letters]:
            translate.append((letter, number))
            
        IPs = re.finditer(pattern_ip, html)
        for ip, port in [x.groups() for x in IPs]:
            port = port.replace('+', '')
            for letter, number in translate:
                port = port.replace(letter, number)
            print "%s:%s" % (ip, port)
        
        
    except:
        break
