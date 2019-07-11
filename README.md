# Biliget 模块档案
## 安装
在cmd中输入以下命令安装

    pip install biliget

在python环境中，需要这样导入

    from bilihelper import biliget

## 模块介绍
#### 这个模块分为两个类

| 类名  | 功效  |
| :-: | :-: |
| Videoget( aid )  | 视频信息操作  |
| Userget( uid ) | 用户信息操作 |

### 他们方法有

#### Videoget( aid )：

| 方法  | 回调  | 返回类型 |
| :------------: | :------------: |  :------------: |
| id()  | 用户id  | int |
| view()  | 观看数  | int |
| dan() | 弹幕数  | int |
| reply() | 评论数  | int |
| favorite()  | 收藏数  | int |
| coin()  | 硬币数  | int |
| share()  | 分享数  | int |
| like()  | 点赞数  | int |
| copyright()  | 版权状态  |int|
| detail()  | 详细信息  |json|
| ownerid()  | 视频主人id  |int|
| title()  |  视频标题 |str|
| cover()  | 视频封面url  |str|
| desc() |  视频简介  |str|

#### Userget( uid ):

| 方法  | 回调  | 返回类型 |
| :------------: | :------------: | :------------: |
| userinfo()  | 用户一般信息  | json  |
|  id() | 用户uid  | int  |
| following(self)  | 用户关注数  | int  |
| whisper(self)  | 用户私信数（无法获取）  | int  |
| black(self)  | 用户黑名单数 （无法获取） |  int |
| follower(self)  | 用户粉丝数  |  int |
|  upinfo(self) | 用户具体信息  | json  |
| username(self)  | 用户名  | str  |
| sex(self)  |  用户性别 男or女 | str  |
| face(self)  | 用户头像链接  | str  |
| sign(self)  | 用户个性签名  | str  |
| level(self)  | 用户等级  | int  |
| birthday(self)  | 用户生日 mm-dd  | str  |
| badge(self)  | 用户是否自己的粉丝勋章  | bool  |
| intr(self)  | 用户的认证信息  | str  |
| viptype(self)  | 用户vip类别 0:无  1:普通VIP 2:年费VIP| int  |
| vipthemetype(self)  |  vip主题状态 | bool  |
| isfollowed(self)  | 是否可以被直接关注  | bool  |
| toppic(self)  |  主页顶部图片url | str  |
| liveinfo(self)  | 直播信息汇总  |  json |
| liveurl(self)  | 直播间链接  | str  |
| liveroomid(self)  |  直播间号 |  int |
| liveroomcover(self)  |直播间封面链接   | str  |
| uservideoinfo(self)  | 用户视频标签  |  list |
| usertags(self)  | 视频页面信息  | json  |
| newv(self)  |   用户最新视频id | int  |
