# coding=utf-8

import os
import time
import requests

def get_skin_list(json_url):
    try:
        r = requests.get(json_url, timeout=20)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.json()
    except Exception as e:
        print('Error: ', e)
        return []

def download_skin(hero_dict, save_dir):
    # hero_dict 人物信息，字典类型
    # save_dir 皮肤保存位置
    hero_ename = str(hero_dict['ename'])
    skin_names = hero_dict['skin_name'].split('|')
    hero_skin_num = len(skin_names)
    for skin_no in range(1,hero_skin_num+1):
        skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' 
        skin_url += hero_ename + '/' + hero_ename + '-bigskin-' + str(skin_no) + '.jpg'
        save_file_name = hero_ename + '-' + hero_dict['cname']+ '-' + skin_names[skin_no-1] + '.jpg'
        save_file_name = os.path.join(save_dir, save_file_name)
        # 文件不存在 或 文件长度为0时，下载数据
        if not os.path.exists(save_file_name) or os.path.getsize(save_file_name) == 0:
            print('正在下载：{} ...'.format(os.path.basename(save_file_name)))
            get_img_data(skin_url, save_file_name)
            time.sleep(0.5)
        else:
            print('文件已存在：{} ...'.format(os.path.basename(save_file_name)))

def get_img_data(img_url,file_name):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
    try:
        r = requests.get(img_url, headers=headers, timeout=20)
        r.raise_for_status()
        if r.status_code == 200:
            with open(file_name, 'wb') as fw:
                fw.write(r.content)
    except Exception as e:
        print('Error: ', e)
        return

if __name__ == '__main__':
    skin_json_url = 'http://pvp.qq.com/web201605/js/herolist.json'
    skin_save_dir = 'wzmnz/source/hero'
    skin_save_dir = os.path.join(os.getcwd(),skin_save_dir)
    if not os.path.exists(skin_save_dir):
        os.mkdir(skin_save_dir)
    hero_infos = get_skin_list(skin_json_url)
    for hero_info in hero_infos:
        download_skin(hero_info, skin_save_dir)
    print('Done!')