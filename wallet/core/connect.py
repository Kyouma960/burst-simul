import requests

post_url = 'http://134.122.95.105:4757/post'
get_url = 'http://134.122.95.105:4757/get'
headers = {"Content-Type": "application/json"}

def post_req(data):
    req = requests.post(post_url,headers=headers, json = data)
    return req

def get_req(data):
    req = requests.get(get_url, json = data)
    return req
