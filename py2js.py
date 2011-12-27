
import re


class py_action:
    def __init__(self, js = ""):
        self.js = js # source js code
        self.translators = [self.tr_var] # translation operations
        self.vars = [] # already defined vars
        
        #~ REs = {}
        #~ REs['name'] = r"[\w][\w\d_]*"
        #~ REs['instance']
        
        
    @property
    def py(self):
        py = self.js
        for translator inself.translators:
            py = translator(py)
        return py
        
    #~ @static
    #~ def tr_var(str):
        #~ if self.REs



