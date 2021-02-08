# encoding:utf-8
import os
import requests
import urllib

def main():
    url = "http://192.168.1.253/small/html/report/wipbyorder/h_id/1/li_id/2"

    payload = {
        "getval": 1,
        "process_plan": "全部",
        "customer_code": "CHW",
        "yewu_em_num": "A030",
        "WIP_type": "含R-lot",
    }

    payload = urllib.parse.urlencode(payload)

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Origin": "http://192.168.1.253",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "PHPSESSID=qkdauu1d3oaj4p2d5gpii7uue2",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    content_type = response.headers['content-type']
    print(content_type)
    return

    html_path = "test.html"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    os.startfile(html_path)
    # print(response.text)

if __name__ == "__main__":
    main()