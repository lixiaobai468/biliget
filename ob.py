import requests
import json
import matplotlib.pyplot as plt
import numpy as np

class Fanslook:
    def __init__(self,page=5):
        self.__doc__ = '数据来源：biliob.com \n 网站作者：Jannchie见齐'

        self.headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36",
        }
        self.burl = 'https://www.biliob.com/api/event/fans-variation?pagesize=' + str(page)

        self.fjson = json.loads(requests.get(self.burl,headers=self.headers).text)
        self.case = self.fjson['content']
        self.fans_list = [[p["author"],p["mid"],p["variation"]] for p in self.case ]
    
    def fans(self):
        return self.fans_list

    def copyright(self):
        print('''
        数据来源：biliob.com \n 
        网站作者：Jannchie见齐 \n
        模块作者:Lixiaobai
        ''')

class Bilitime:
    def __init__(self):
        self.headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36",
        }
        self.turl = 'https://www.biliob.com/api/site'
        self.tjson = json.loads(requests.get(self.turl,headers=self.headers).text)

        self.playlist = [playitem['playOnline'] for playitem in self.tjson]
        self.weblist = [playitem['webOnline'] for playitem in self.tjson]
        self.datelist = [playitem['datetime'] for playitem in self.tjson]

    def draw(self):
        plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

        plt.title("在线人数，观看数曲线") 
        
        x1 = np.array([i+1 for i in range(len(self.playlist))][::-1])
        y1 = np.array(self.playlist)
        plt.plot(x1,y1,color = 'dodgerblue',label = "播放人数")# 折线 1 x 2 y 3 color

        x2 = np.array([i+1 for i in range(len(self.weblist))][::-1])
        y2 = np.array(self.weblist)
        plt.plot(x2,y2,color = 'r',label = "在线人数")# 折线 1 x 2 y 3 color

        plt.show()
    
    def zipped(self):
        self.zipper =[]
        for i in range(len(self.playlist)):
            self.zipper.append([self.playlist[i],self.weblist[i],self.datelist[i]])
        return self.zipper
