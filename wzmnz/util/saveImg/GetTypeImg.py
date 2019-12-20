# coding=utf-8

import os
import time
import random
import requests


# 获取所有的uri http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
# base_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
# skin_save_dir = os.path.join(os.getcwd(),skin_save_dir)

def get_img_list():
    img_uri_list = []
    file_path = os.path.join(os.getcwd(), 'wzmnz\config\img_uri.txt')
    f = open(file_path, 'r')
    img_uri_list = f.read().splitlines()
    return img_uri_list


def download_img(img_uri, skin_save_dir):
    save_file_name = os.path.join(skin_save_dir, ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)) + '.png')
    if not os.path.exists(save_file_name) or os.path.getsize(save_file_name) == 0:
            print('正在下载：{} ...'.format(os.path.basename(save_file_name)))
            get_img_data(img_uri, save_file_name)
            time.sleep(0.5)
    else:
        print('文件已存在：{} ...'.format(os.path.basename(save_file_name)))

def get_img_data(img_uri,file_name):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
    try:
        r = requests.get(img_uri, headers=headers, timeout=20)
        r.raise_for_status()
        if r.status_code == 200:
            with open(file_name, 'wb') as fw:
                fw.write(r.content)
    except Exception as e:
        print('Error: ', e)
        return

if __name__ == '__main__':
    skin_save_dir = 'wzmnz/source/type'
    skin_save_dir = os.path.join(os.getcwd(), skin_save_dir)
    if not os.path.exists(skin_save_dir):
        os.mkdir(skin_save_dir)
    img_uri_list = get_img_list()
    for img_uri in img_uri_list:
        download_img(img_uri, skin_save_dir)
    print('Done!')
