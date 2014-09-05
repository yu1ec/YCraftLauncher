'''
Created on 2014年9月5日

@author: EcareYu
'''

from APIs import Resource
from urllib import parse,request,error

class Utility(object):
    '''
    Some global methods
    '''
    
    def checkServerStatus(self):
        #TODO check the minecraft server status
         
        print('ok')
        pass       
    
    def httpPost(self,url,params,header=None):
        pass
    
    def httpGet(self,url,params=None,header=None):
        try:
            if(None != params):
                params = parse.urlencode(params)
            request.urlopen(url,data=params)
        except error.URLError as urlErr:
            #TOTO write logs
            pass
        except error.HTTPError as httpErr:
            #TOTO write logs
            pass
             