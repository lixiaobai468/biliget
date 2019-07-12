# Biliget 模块档案
## 安装
在cmd中输入以下命令安装

    pip install biliget
    python3 -m pip install biliget

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
| following()  | 用户关注数  | int  |
| whisper()  | 用户私信数（无法获取）  | int  |
| black()  | 用户黑名单数 （无法获取） |  int |# Biliget 模块档案# Biliget 模块档案


## 安装


在cmd中输入以下命令安装

    pip install biliget
    python3 -m pip install biliget


我们提供三个包  basics,fun,ob

在python环境中，需要这样导入

    from biliget import basics
	from biliget import fun
	from biliget import ob

--------------------------------


# 模块介绍


### basics 这个包分为两个类

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
| following()  | 用户关注数  | int  |
| whisper()  | 用户私信数（无法获取）  | int  |
| black()  | 用户黑名单数 （无法获取） |  int |
| follower()  | 用户粉丝数  |  int |
|  upinfo() | 用户具体信息  | json  |
| username()  | 用户名  | str  |
| sex()  |  用户性别 男or女 | str  |
| face()  | 用户头像链接  | str  |
| sign()  | 用户个性签名  | str  |
| level()  | 用户等级  | int  |
| birthday()  | 用户生日 mm-dd  | str  |
| badge()  | 用户是否自己的粉丝勋章  | bool  |
| intr()  | 用户的认证信息  | str  |
| viptype()  | 用户vip类别 0:无  1:普通VIP 2:年费VIP| int  |
| vipthemetype()  |  vip主题状态 | bool  |
| isfollowed()  | 是否可以被直接关注  | bool  |
| toppic()  |  主页顶部图片url | str  |
| liveinfo()  | 直播信息汇总  |  json |
| liveurl()  | 直播间链接  | str  |
| liveroomid()  |  直播间号 |  int |
| liveroomcover()  |直播间封面链接   | str  |
| uservideoinfo()  | 用户视频标签  |  list |
| usertags()  | 视频页面信息  | json  |
| newv()  |   用户最新视频id | int  |


### fun这个包有一个类

| 类名  | 功效  |
| :-: | :-: |
| Ds()| 获取本站默认搜索内容 |

#### 他有以下方法

| 方法  | 回调  | 返回类型 |
| :------------: | :------------: |  :------------: |
| showname()  | 返回搜索框内容文字  | str |
| dstype()  | 返回指向页面类型 1为视频  | int |
| value() | 判断类型并给出值$^1$  | list |
| url() | 返回指向url  | str |
| all()  | 关于默认搜索的所有内容  | json |

1:  
 如果为视频： ['video',aid] || aid->int
 

 如果为其他： ['other',...]


###ob这个包有一个类

| 类名  | 功效  |
| :-: | :-: |
| Fanslook(pagesize)$^2$ | 获取最近值得关注的up主 |
2：
pagesize决定返回值的项数，可选，默认值为5 (详见输出值)

#### 他有以下方法


| 方法  | 回调  | 返回类型 |
| :------------: | :------------: |  :------------: |
| fans()  | 获取最近值得关注的up主粉丝数以及uid  | list |
| \__copyright__()  | 版权说明  | print() |

#### fans()的返回值

    [['点滴菌', 102885422, -6150], ... ]
    
    #这是一个list包裹多个list的结构
    #内部list的结构： 第一项-up名字  第二项-up的uid  第三项-粉丝变化









## 安装
在cmd中输入以下命令安装

    pip install biliget
    python3 -m pip install biliget


我们提供三个包  basics,fun,ob

在python环境中，需要这样导入

    from biliget import basics
	from biliget import fun
	from biliget import ob

--------------------------------
# 模块介绍
### basics 这个包分为两个类

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
| following()  | 用户关注数  | int  |
| whisper()  | 用户私信数（无法获取）  | int  |
| black()  | 用户黑名单数 （无法获取） |  int |
| follower()  | 用户粉丝数  |  int |
|  upinfo() | 用户具体信息  | json  |
| username()  | 用户名  | str  |
| sex()  |  用户性别 男or女 | str  |
| face()  | 用户头像链接  | str  |
| sign()  | 用户个性签名  | str  |
| level()  | 用户等级  | int  |
| birthday()  | 用户生日 mm-dd  | str  |
| badge()  | 用户是否自己的粉丝勋章  | bool  |
| intr()  | 用户的认证信息  | str  |
| viptype()  | 用户vip类别 0:无  1:普通VIP 2:年费VIP| int  |
| vipthemetype()  |  vip主题状态 | bool  |
| isfollowed()  | 是否可以被直接关注  | bool  |
| toppic()  |  主页顶部图片url | str  |
| liveinfo()  | 直播信息汇总  |  json |
| liveurl()  | 直播间链接  | str  |
| liveroomid()  |  直播间号 |  int |
| liveroomcover()  |直播间封面链接   | str  |
| uservideoinfo()  | 用户视频标签  |  list |
| usertags()  | 视频页面信息  | json  |
| newv()  |   用户最新视频id | int  |


### fun这个包有一个类

| 类名  | 功效  |
| :-: | :-: |
| Ds()| 获取本站默认搜索内容 |

####他有以下方法

| 方法  | 回调  | 返回类型 |
| :------------: | :------------: |  :------------: |
| showname()  | 返回搜索框内容文字  | str |
| dstype()  | 返回指向页面类型 1为视频  | int |
| value() | 判断类型并给出值$^1$  | list |
| url() | 返回指向url  | str |
| all()  | 关于默认搜索的所有内容  | json |

1:  
 如果为视频： ['video',aid] || aid->int 
 如果为其他： ['other',...]


### ob这个包有一个类

| 类名  | 功效  |
| :-: | :-: |
| Fanslook(pagesize)$^2$ | 获取最近值得关注的up主 |
2：
pagesize决定返回值的项数，可选，默认值为5 (详见输出值)

#### 他有以下方法


| 方法  | 回调  | 返回类型 |
| :------------: | :------------: |  :------------: |
| fans()  | 获取最近值得关注的up主粉丝数以及uid  | list |
|___copyrigt___() | 版权说明  | print() |

#### fans()的返回值

    [['点滴菌', 102885422, -6150], ... ]
    
    #这是一个list包裹多个list的结构
    #内部list的结构： 第一项-up名字  第二项-up的uid  第三项-粉丝变化






