# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-02-09 10:58:36"

import time
import json
import urllib
import requests
import pandas as pd

import lxml
import openpyxl

class DataDumper(object):

    @classmethod
    def test_dump(cls):
        cls.dump_outcoming()
        cls.dump_inventory()
        cls.dump_incoming()
        cls.dump_progress()
        
    
    @classmethod
    def dump_outcoming(cls, filename="出库报表.xlsx"):
        """
        出库报表
        """

        start_date = "%s-01" % time.strftime("%Y-%m", time.localtime())
        end_date = time.strftime("%Y-%m-%d", time.localtime())
        customer_code = "CHW"
        url = f"http://192.168.1.253/small/html/yw/outprintcontent?customer_code={customer_code}&customer_po=&po=&cp_name=&kaidan_name=&cp_gg=&lotno=2&start_date={start_date}&end_date={end_date}"

        payload = {}
        headers = {
            "Cookie": "PHPSESSID=0lsdr3jh8benspp3kk45v753j1; PHPSESSID=kr59clpbibcugadmorf9la1j73",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
            "Accept": "text/html, */*; q=0.01",
            "Referer": "http://192.168.1.253/small/html/yw/outprint/disable/1/height/674",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.encoding = "utf-8"
        table = pd.read_html(response.text)[-1]
        table.to_excel(filename)

    @classmethod
    def dump_inventory(cls, filename="库存明细.xlsx"):
        """
        库存明细
        """

        customer_code = "CHW"
        url = f"http://192.168.1.253/small/html/ckcp/getckcpdetail?cp_name=&customer_code={customer_code}&customer_po=&po=&pageSize=50&pageNumber=1&page=1&rows=50&sort=id&order=DESC"

        payload = {}
        headers = {
            "Cookie": "PHPSESSID=4h36l6pt9dg3s44ia3u4seg7e0; PHPSESSID=kr59clpbibcugadmorf9la1j73",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Referer": "http://192.168.1.253/small/html/ckcp/cpdetail/type/out/disable/1/height/674",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        
        json_data = json.loads(response.text)

        data = [
            [
                row.get("device_type", ""),
                row.get("kaidan_name", ""),
                row.get("bin_remark", ""),
                row.get("marking_num", ""),
                row.get("price", ""),
                row.get("qty", ""),
                row.get("customer_code", ""),
                row.get("customer_name", ""),
                row.get("product_tm", ""),
                row.get("customer_po", ""),
                row.get("po", ""),
                row.get("lotno", ""),
                row.get("opt", ""),
                row.get("opt_name", ""),
                row.get("add_time", ""),
            ]
            for row in json_data["rows"]
        ]

        df = pd.DataFrame(
            data,
            columns=[
                "产品名称",
                "开单型号",
                "类型",
                "丝印编号",
                "单价",
                "数量",
                "客户代码",
                "客户名称",
                "线图编号",
                "委工单号",
                "制造单号",
                "批次号",
                "工号",
                "姓名",
                "添加时间",
            ],
        )
        
        df.to_excel(filename)

    @classmethod
    def dump_incoming(cls, filename="入库报表.xlsx"):
        """
        入库报表
        """
        start_date = "%s-01" % time.strftime("%Y-%m", time.localtime())
        end_date = time.strftime("%Y-%m-%d", time.localtime())
        customer_code = "CHW"
        url = f"http://192.168.1.253/small/html/ckcp/inprintcontent?customer_code={customer_code}&customer_po=&po=&cp_name=&kaidan_name=&cp_gg=&lotno=2&start_date={start_date}&end_date={end_date}"

        payload = {}
        headers = {
            "Cookie": "PHPSESSID=vqrr9itgn8uelru2rno7o1smb2",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.encoding = "utf-8"

        table = pd.read_html(response.text)[-1]
        table.to_excel(filename)

    @classmethod
    def dump_progress(cls, filename="生产进度表.xlsx"):
        """
        生产进度表
        """
        customer_code = "CHW"
        url = "http://192.168.1.253/small/html/report/wipbyorder/h_id/1/li_id/2"
        payload = {
            "getval": 1,
            "process_plan": "全部",
            "customer_code": customer_code,
            "yewu_em_num": "A030",
            "WIP_type": "含R-lot",
        }

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
            # "Cookie": "PHPSESSID=qkdauu1d3oaj4p2d5gpii7uue2",
        }
        payload = urllib.parse.urlencode(payload)
        response = requests.request("POST", url, headers=headers, data=payload)
        response.encoding = "utf-8"
        html = response.text

        table = pd.read_html(html)[-1]
        # table.iloc[1] = table.iloc[1].shift(18)
        table.to_excel(filename)

# DataDumper.test_dump()