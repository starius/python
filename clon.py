# -*- coding: cp1251 -*-

####################################
#   Create new clon of list or dict
####################################


def clon (obj):
    t = type(obj)


    if t == list or t == tuple:
        
        r = []
        
        for i in obj:
            r.append(clon(i))

        if t == tuple:
            r = tuple(r)

        return r


    if t == dict:
        
        r = {}
        
        for key, value in obj.items():
            r[key] = clon(value)


        return r

    return obj

            
    
