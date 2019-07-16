import  requests
import json

class Ds:
    def __init__(self):
        self.__doc__ = '返回搜索框默认内容'
        self.burl = 'https://api.bilibili.com/x/web-interface/search/default'
        self.ds_json = json.loads(requests.get(self.burl).text)
        self.dstypenum = self.ds_json['data']['goto_type']

    def showname(self):
        '''
        返回搜索框内容 str
        '''
        return self.ds_json['data']['show_name']
    
    def dstype(self):
        '''
        返回指向页面类型 1为视频 int
        '''
        return self.dstypenum

    def value(self):
        '''
        判断类型并给出值
        如果为视频： ['video',aid] || aid->int
        如果为其他： ['other',...]
        '''
        if self.dstypenum == 1:
            return ['video',int(self.ds_json['data']['goto_value'])]
        else:
            return ['other',self.ds_json['data']['goto_value']]

    def url(self):
        '''
        返回指向url
        '''
        return self.ds_json['data']['url']

    def all(self):
        return self.ds_json
