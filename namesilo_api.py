#!/bin/python3

'''
对namesilo网站提供的api进行操作
提供查询、更改、增加、删除域名dns记录的功能

To operate the API provided by Nameilo Website.
Provide the function of querying, changing, adding and deleting DNS records 
of domain name.
=======================================
！！使用前需要修改API key ！！
!! need to change API key before use !!
=======================================
Copyright (c) [2020] [bobwxc]
[namesilo_api_shell] is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan 
PSL v2.You may obtain a copy of Mulan PSL v2 at:
        http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
-------------------------------------
同时适用：
反996许可证版本1.0
        https://github.com/996icu/996.ICU/blob/master/LICENSE_CN
-------------------------------------
Namesilo is a mark of Namesilo Co.Ltd
'''

import xml.etree.ElementTree as et

import requests

# global variable
key = 'xxxxxxxxxxxxxxx'


def dnsListRecords(domain, printflag):

    url = 'https://www.namesilo.com/api/dnsListRecords?version=1&type=xml&key=' + \
        key+'&domain='+domain
    if printflag == 1:
        print('request url:', url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    xml = r.content.decode('utf-8')
    print('-------\n', xml, '-------')
    '''
    <namesilo>
    <request>
        <operation>dnsListRecords</operation>
        <ip>55.555.55.55</ip>
    </request>
    <reply>
        <code>300</code>
        <detail>success</detail>
        <resource_record>
            <record_id>1a2b3c4d5e6f</record_id>
            <type>A</type>
            <host>test.namesilo.com</host>
            <value>55.555.55.55</value>
            <ttl>7207</ttl>
            <distance>0</distance>
        </resource_record>
        <resource_record>
            <record_id>5Brg5hw25jr</record_id>
            <type>CNAME</type>
            <host>dev.namesilo.com</host>
            <value>testing.namesilo.com</value>
            <ttl>7207</ttl>
            <distance>0</distance>
        </resource_record>
        <resource_record>
            <record_id>fH35aH4hsv</record_id>
            <type>MX</type>
            <host>namesilo.com</host>
            <value>mail.namesilo.com</value>
            <ttl>7207</ttl>
            <distance>10</distance>
        </resource_record>
        <resource_record>
            <record_id>Ldfd26Sfbh</record_id>
            <type>MX</type>
            <host>namesilo.com</host>
            <value>mail2.namesilo.com</value>
            <ttl>7207</ttl>
            <distance>20</distance>
        </resource_record>
    </reply>
    </namesilo>
    '''
    root = et.fromstring(xml)
    dnsList = []
    i = 0
    for child in root:
        if child.tag == 'reply':
            if printflag == 1:
                print("-------")
            for child1 in child:
                if child1.tag == 'resource_record':
                    dnsinfo = {}
                    if printflag == 1:
                        i += 1
                        print(i)
                    for child2 in child1:
                        if printflag == 1:
                            print(child2.tag, ':', child2.text)
                        dnsinfo[child2.tag] = child2.text
                    if printflag == 1:
                        print("-------")

                    dnsList.append(dnsinfo)
    if printflag == 1:
        print('total:', i, '\n-------')
    return(dnsList, i)


def dnsUpdateRecord(domain, rrid, rrhost, rrvalue, rrttl):
    print('domain:', domain)
    print('rrid', rrid)
    print('rrhost', rrhost)
    if rrhost.find(domain) != -1:
        rrhost = rrhost[0:len(rrhost)-len(domain)-1]

    url = 'https://www.namesilo.com/api/dnsUpdateRecord?version=1&type=xml&key='+key + \
        '&domain='+domain+'&rrid='+rrid+'&rrhost=' + \
        rrhost+'&rrvalue='+rrvalue+'&rrttl='+rrttl
    print('request url:', url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    xml = r.content.decode('utf-8')
    print('-------\n', xml, '-------')

    """
    <namesilo>
        <request>
            <operation>dnsUpdateRecord</operation>
            <ip>55.555.55.55</ip>
        </request>
        <reply>
            <code>300</code>
            <detail>success</detail>
            <record_id>1a2b3c4d5e</record_id>
        </reply>
    </namesilo> 
    """

    root = et.fromstring(xml)

    for child in root:
        if child.tag == 'reply':
            for child1 in child:
                if child1.tag == 'detail':
                    return(child1.text)


def dnsAddRecord(domain, rrtype, rrhost, rrvalue, rrttl):
    print('domain:', domain)
    if rrhost.find(domain) != -1:
        rrhost = rrhost[0:len(rrhost)-len(domain)-1]

    url = 'https://www.namesilo.com/api/dnsAddRecord?version=1&type=xml&key='+key + \
        '&domain='+domain+'&rrtype='+rrtype+'&rrhost=' + \
        rrhost+'&rrvalue='+rrvalue+'&rrttl='+rrttl
    print('request url:', url)
    header = {
        'User-Agent': 'Mozilla/6.0 (Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    r = requests.get(url, headers=header)
    xml = r.content.decode('utf-8')
    print('-------\n', xml, '-------')

    """ 
    <namesilo>
        <request>
            <operation>dnsAddRecord</operation>
            <ip>55.555.55.55</ip>
        </request>
        <reply>
            <code>300</code>
            <detail>success</detail>
            <record_id>1a2b3c4d5e</record_id>
        </reply>
    </namesilo>   
    """
    root = et.fromstring(xml)

    for child in root:
        if child.tag == 'reply':
            for child1 in child:
                if child1.tag == 'detail':
                    return(child1.text)


def dnsDeleteRecord(domain, rrid):
    print('domain:', domain)

    url = 'https://www.namesilo.com/api/dnsDeleteRecord?version=1&type=xml&key=' + \
        key+'&domain='+domain+'&rrid='+rrid

    print('request url:', url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    xml = r.content.decode('utf-8')
    print('-------', xml, '-------')

    """ 
    <namesilo>
        <request>
            <operation>dnsDeleteRecord</operation>
            <ip>55.555.55.55</ip>
        </request>
        <reply>
            <code>300</code>
            <detail>success</detail>
        </reply>
    </namesilo>
    """
    root = et.fromstring(xml)

    for child in root:
        if child.tag == 'reply':
            for child1 in child:
                if child1.tag == 'detail':
                    return(child1.text)


def main():
    domain = input("enter the root domain: ")
    (dnslist, n) = dnsListRecords(domain, 1)
    # print(dnslist,n)
    # [{'type': 'CNAME', 'host': 'www.DOMAIN', 'value': 'xxxxx', 'record_id': 'c81d8b8587798f78xxxxxxxxx', 'distance': '0', 'ttl': '3600'}, {'type': 'TXT', 'host': '_domainconnect.DOMAIN', 'value': 'www.namesilo.com/domainconnect', 'record_id': 'c44ba964cf241121xxxxxxxxx', 'distance': '0', 'ttl': '3600'}]

    while(1):
        print("choose mode:(use 0 to exit)\n1. add\n2. delete\n3. update\n4. list")
        a = input()
        if a == '0':
            break
        elif a == '1':
            rrtype = input(
                "enter the rrtype: (\"A\", \"AAAA\", \"CNAME\", \"MX\" and \"TXT\")")
            rrhost = input("enter the rrhost: ")
            rrvalue = input("enter the rrvalue: ")
            rrttl = input("enter the rrttl: ")
            print(dnsAddRecord(domain, rrtype, rrhost, rrvalue, rrttl))
        elif a == '2':
            pass
            nn = int(input("enter the No.: "))
            print("are you sure to delete\n",
                  dnslist[nn-1], "\n? (Y/y or N/n)")
            aa = input()
            if aa == 'Y' or aa == 'y':
                print(dnsDeleteRecord(domain, dnslist[nn-1]['record_id']))
            else:
                print('cancel')
        elif a == '3':
            nn = int(input("enter the No.: "))
            rrvalue = input("enter the rrvalue: ")
            rrttl = input("enter the rrttl: ")
            print(dnsUpdateRecord(
                domain, dnslist[nn-1]['record_id'], dnslist[nn-1]['host'], rrvalue, rrttl))
        elif a == '4':
            (dnslist, n) = dnsListRecords(domain, 1)
        else:
            print("enter error,redo")

    print('bye')


if __name__ == "__main__":
    main()
