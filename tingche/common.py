import time
import random
import string

# 获取13位时间戳
def current_timestr13():
    return str(int(round(time.time() * 1000)))

def get8randomstr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8)).lower()

def get11digits():
    return ''.join(random.sample(string.digits, 8))+''.join(random.sample(string.digits, 3))

def get8digits():
    return ''.join(random.sample(string.digits, 8))

def get_upper_12str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 12)).upper()


def get_upper_32str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 32)).upper()

def get32str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 32)).lower()

def jieting_cookie():
    #  "UM_distinctid=173704b38d8e6-048ac12f1288c7-470f6e5f-3d10d-173704b38da102"
    return 'UM_distinctid=173704b38d8e6-'+''.join(random.sample(string.ascii_letters + string.digits, 14)).lower()+'-470f6e5f-3d10d-173704b38da102'

def getrandomstr():
    ran_8str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    ran_28str = ''.join(random.sample(string.ascii_letters + string.digits, 28))
    return current_timestr13()+ran_8str+'_'+ran_28str

# 获取随机的useragent
def getrandom_useragent():
    useragents = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e25) NetType/WIFI Language/zh_CN miniProgram",
        'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
        'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
        'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
        'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
        'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c30) NetType/WIFI Language/zh_CN',

    ]
    return random.choice(useragents)