#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sxs
# @Date  : 2018/6/20
# @Desc  :
import requests
from bs4 import BeautifulSoup
import time
import json

diary_home_url = 'https://tower.im/projects/122a4eafcf1643f6bec2bba9d776fc7f/lists/3593325114fa41348025e83e2579d1c4/show/'
my_diary = 'https://tower.im/projects/122a4eafcf1643f6bec2bba9d776fc7f/todos/fd8d943c60644147bd8cb0d3d36dc66b/comments'
test_url = 'https://tower.im/projects/29fa2bc07a984a84aed9e3593d507c25/todos/aaf2644e670f4695ae2c1f80a977be04/comments'

headers = {
    'X-CSRF-Token': 'f1QtY5A7L4LCKx0U8mTXa1Ke5nolnOL20NVTIAC1ZX8/B0KMONeWYgbiz0Cijga4a/Hm6ZpHjGhhfDIKipEonA==',
}

cookies = {
    'Cookie':
        'remember_token=26bcc67f-d848-457a-a9da-11025384b70c;'
        '_tower2_session=8670f55da338c2d135e56c0b4bae8b00;'
}
my_diary_data = {
    '已完成:': '',
    '进行中:': '',
    '未完成:': '',
    '明日任务:': '',
}
my_diary_request = {
    'conn_guid': '7fdb35b9-c834-4d5c-9493-223a5a9720b1',
    'is_html': 1,
    'cc_guids': '',
    'attach_guids': '',
    'delete_attach_guids': '',
    'attach_order': ''
}

username = {'但彬': '', '徐善栋': '', '曹世鑫': '', '方俊': '', '李杰': '', '沈晓顺': ''}
# 当日时间
today = time.strftime("%Y-%m-%d", time.localtime())


def get_diary_url():
    diary_result = requests.get(diary_home_url, cookies=cookies)
    soup = BeautifulSoup(diary_result.text, 'lxml')
    home_links = soup.select('div.todo-wrap')
    for item in home_links:
        for key in username:
            if key in item.get_text():
                username[key] = item.select('span.todo-content > span.content-linkable > a')[0].get('href')


# 检查日报完成情况
def check_diary():
    get_diary_url()
    for key in username:
        user_diary = requests.get(username.get(key), cookies=cookies)
        soup = BeautifulSoup(user_diary.text, 'lxml')
        write_time = soup.select('div.comment-main > div.info > a.create-time')
        if today in str(write_time[- 1]):
            username[key] = ''
        else:
            username[key] = '日报没写'
    print(username)


# 写日报
def write_my_diary():
    for key in my_diary_data:
        print(key)
        my_diary_data[key] = input()
    my_diary_request['comment_content'] = format_to_html(my_diary_data)
    result = requests.post(my_diary, headers=headers, cookies=cookies, data=my_diary_request)
    if result.status_code == 200:
        print(today, '日报发送成功')
    else:
        print(result.status_code, today, '日报发送失败')


# 日报内容转成html
def format_to_html(data):
    html = '<p>{}</p>'.format(today + "日报")
    for key in data.keys():
        html += "<p>{0}</p><p>{1}</p>".format(key, data.get(key))
    return html


if __name__ == '__main__':
    # check_diary()
    write_my_diary()
