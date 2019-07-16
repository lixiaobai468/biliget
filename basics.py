import requests
import json

class Userget:
    def __init__(self,uid):
        self.uid = str(uid)
        self.headers = {
        "User-Agent":"Bili fans/1.0.0 (18108274905@163.com)",
        "Host":"api.bilibili.com",
        "Connection":"keep-alive"
        }
        #获取账户信息
        self.info_url = 'https://api.bilibili.com/x/relation/stat?jsonp=jsonp&vmid=' + self.uid
        self.user_info_j = json.loads(requests.get(self.info_url,headers=self.headers).text)
        
        #up信息
        self.upinfo_url = "https://api.bilibili.com/x/space/acc/info?mid="+ self.uid +"&jsonp=jsonp"
        self.up_info_j = json.loads(requests.get(self.upinfo_url,headers=self.headers).text)

        #获取直播信息
        self.live_url = "https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid=" + self.uid
        self.user_live_j = json.loads(requests.get(self.live_url).text)

        #大体视频信息
        self.video_list_url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=" + self.uid
        self.big_video_j = json.loads(requests.get(self.video_list_url).text)




    #账户信息回调
    def userinfo(self):
        '''
        用户一般信息json
        '''
        return self.user_info_j

    def id(self):
        '''
        用户uid int
        '''
        return self.user_info_j['data']['mid']

    def following(self):
        '''
        用户关注数 int 
        '''
        return self.user_info_j['data']['following']

    def whisper(self):
        '''
        用户私信数 int 一般无法获取
        '''
        return self.user_info_j['data']['whisper']

    def black(self):
        '''
        用户黑名单数 int
        '''
        return self.user_info_j['data']['black']

    def follower(self):
        '''
        用户粉丝数 int
        '''
        return self.user_info_j['data']['follower']

    #up信息回调
    def upinfo(self):
        '''
        用户具体信息json
        '''
        return self.up_info_j
    
    def username(self):
        '''
        用户名 str
        '''
        return self.up_info_j['data']['name']

    def sex(self):
        '''
        用户性别 str 
        '''
        return self.up_info_j['data']['sex']

    def face(self):
        '''
        用户头像链接 str
        '''
        return self.up_info_j['data']['face']
    
    def sign(self):
        '''
        用户个性签名 str
        '''
        return self.up_info_j['data']['sign']
    
    def level(self):
        '''
        用户等级 int
        '''
        return self.up_info_j['data']['level']
    
    def birthday(self):
        '''
        用户生日 mm-dd   str
        '''
        return self.up_info_j['data']['birthday']
    
    def badge(self):
        '''
        用户是否自己的粉丝勋章  Boolean
        '''
        return self.up_info_j['data']['fans_badge']
    
    def intr(self):
        '''
        用户的认证信息 str
        '''
        return self.up_info_j['data']['official']['title']

    def viptype(self):
        '''
        用户vip类别 int
        0:无  1:普通VIP 2:年费VIP
        '''
        return self.up_info_j['data']['vip']['type']

    def vipthemetype(self):
        '''
        vip主题状态 Boolean
        '''
        return self.up_info_j['data']['vip']['theme_type']

    def isfollowed(self):
        '''
        是否可以被直接关注 Boolean
        '''
        return self.up_info_j['data']['is_followed']

    def toppic(self):
        '''
        主页顶部图片url str
        '''
        return self.up_info_j['data']['top_photo']


    #直播信息回调
    def liveinfo(self):
        return self.user_live_j

    def liveurl(self):
        '''
        直播间链接 str
        '''
        return self.user_live_j['data']['url']

    def liveroomid(self):
        '''
        直播间号 int
        '''
        return self.user_live_j['data']['roomid']

    def liveroomcover(self):
        '''
        直播间封面链接 str
        '''
        return self.user_live_j['data']['cover']

    
    #大体视频信息回调
    def uservideoinfo(self):
        return self.big_video_j
    
    def usertags(self):
        '''
        用户视频标签list [str,...]
        '''
        tlist = [tag for tag in self.big_video_j['data']['tlist']]
        tags = [tag for tag in tlist['name']]
        return tags
    
    def newv(self):
        '''
        用户最新视频id int
        '''
        return self.big_video_j['data']['vlist'][0]['aid']


class Videoget:
    def __init__(self,aid):
        self.aid = str(aid)
        self.headers = {
        "User-Agent":"Bili fans/1.0.0 (18108274905@163.com)",
        "Host":"api.bilibili.com",
        "Connection":"keep-alive"
        }
        
        #获取视频基本信息
        self.vnum_url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid=' + self.aid
        self.vnum_j = json.loads(requests.get(self.vnum_url,headers=self.headers).text)

        #获取视频详细信息
        self.vinfo_url = 'https://api.bilibili.com/x/web-interface/view?aid=' + self.aid
        self.vinfo_j = json.loads(requests.get(self.vinfo_url,headers=self.headers).text)

        #获取视频下载信息 kanbilibili.com
        self.vd_url = 'https://www.kanbilibili.com/api/video/'+ self.aid +'/download?cid=101560001&quality=64&page=1'
        self.vd_j = json.loads(requests.get(self.vd_url,headers=self.headers).text)


    #基本信息回调
    def id(self):
        return int(self.vnum_j['data']['aid'])

    def view(self):
        '''
        观看数 int
        '''
        return self.vnum_j['data']['view']

    def dan(self):
        '''
        弹幕数 int 
        '''
        return self.vnum_j['data']['danmaku']
    
    def reply(self):
        '''
        评论数
        '''
        return self.vnum_j['data']['reply']

    def favorite(self):
        '''
        收藏数 int
        '''
        return self.vnum_j['data']['favorite']

    def coin(self):
        '''
        硬币数 int
        '''
        return self.vnum_j['data']['coin']

    def share(self):
        '''
        分享数 int
        '''
        return self.vnum_j['data']['share']
    
    def like(self):
        '''
        点赞数 int
        '''
        return self.vnum_j['data']['like']
    
    def copyright(self):
        '''
        版权状态 int
        '''
        return self.vnum_j['data']['copyright']

    #杂项信息回调
    def detail(self):
        return self.vinfo_j

    def ownerid(self):
        '''
        视频主人id int
        '''
        return self.vinfo_j['data']['owner']['mid']

    def title(self):
        '''
        视频标题 str
        '''
        return self.vinfo_j['data']['title']
    
    def cover(self):
        '''
        视频封面url str
        '''
        return self.vinfo_j['data']['pic']

    def desc(self):
        '''
        视频简介 str
        '''
        return self.vinfo_j['data']['desc']


# class Downv:
    # def __init__(self,aid):
        # self.aid = str(aid)
        # self.headers = {
        # "User-Agent":"Bili fans/1.0.0 (18108274905@163.com)",
        # "Host":"api.bilibili.com",
        # "Connection":"keep-alive"
        # }

        # #获取视频下载信息 kanbilibili.com
        # self.vd_url = 'https://www.kanbilibili.com/api/video/'+ self.aid +'/download?cid=101560001&quality=64&page=1'
        # self.vd_j = json.loads(requests.Session().get(self.vd_url).text)
        # self.dj = self.vd_j['data']['durl'][0] 

    # def url(self):
        # dlist = [self.vd_j['data']['durl'][0]['url'],self.vd_j['data']['durl'][0]['backup_url']]
        # return dlist
    
    # def formats(self):
        # return self.vd_j['data']['format']
    
    # def size(self):
        # return self.dj['size']
    
    # def time(self):
        # return self.dj['length']
