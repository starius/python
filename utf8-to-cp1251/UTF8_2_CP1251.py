
# change encoding of all files


EXTs = ["php", "htm", "html", "txt", "js"]

FROM = "windows-1251"
#FROM = ""

TO = "utf8"



import chardet # http://chardet.feedparser.org/



import os
#import sys





def enc_converter(path):

    try:
        
        sub_dirs = os.listdir(path)

        for sub_dir in sub_dirs:

            enc_converter(path + '/' + sub_dir)

    except:
        # it is file
        
        name = path.split('/')[-1]
        ext = name.split('.')[-1].lower()
        
        if EXTs.count(ext) == 0:
            # it is not our file
            return 
        
        
        # read
        
        text = ''.join(open(path, 'r').readlines())
        
        
        # decode
                
        enc = chardet.detect(text)['encoding']
        
        if enc == TO:
            return # already
            
        if FROM != '':
            enc = FROM
        
        text = unicode(text, enc) # in Unicode
        
        text = text.encode(TO) # in UTF8
        
        
        
        # write
        
        open(path, 'w').write(text)
        
        print enc, path
        
        
        return

enc_converter('./files')

