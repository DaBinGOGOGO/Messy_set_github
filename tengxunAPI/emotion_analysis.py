import hashlib
import time
import random
import string
from urllib.parse import quote
import requests


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    # 将得到的MD5值所有字符转换成大写
    return m.hexdigest().upper()


def get_params(plus_item):
    global params
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）  
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测  
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key  
    app_id = '2122934548'
    app_key = 'Xtrh9m7rZmXKnX5U'
    params = {'app_id': app_id,
              'text': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              }
    sign_before = ''
    # 要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名  
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


def get_sentiments(comments):
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"
    comments = comments.encode('utf-8')
    payload = get_params(comments)
    r = requests.post(url, data=payload)
    return r.json()


if __name__ == '__main__':
    while True:
        comment = input('评论：')
        answer = get_sentiments(comment)
        if answer['ret'] == 0:
            print('输入成功')
            print(answer['data']['text'])
            print('情感倾向：', answer['data']['polar'], '置信度：', answer['data']['confd'])
        else:
            print('请重新输入')
        print(answer)
        # print('机器人：' + answer)

# 这家店的鱼香肉丝很好吃啊
# 这件衣服很适合我，穿起来软软的。
# 你真的很傻逼啊
