# coding:utf8

# git pull 保证git项目的文件永远是最新的
# 将配置的路径内容对比git项目中的文件
# 制定一个标准发现是git项目中的文件是最新 还是配置路径的文件是最新
# （问题git和配置路径中同时都有修改，概率较小。此脚本一直在运行，保证git中文件一直同步到配置路径中）
# 将配置的路径内容拷贝到git项目中,进行备份push 或者git项目中的文件覆盖到配置路径中
import os

configs = {
    "backups":
        {
            "/opt/app/yun-config/application/idea/settings.zip": "/opt/app/idea/settings.zip",
            "/opt/app/yun-config/application/vscode/settings.json": "/opt/app/vscode/settings.zip"
        },
    "git_project_path": "/opt/app/yun-config"
}


def git_pull():
    git_project_path = configs['git_project_path']
    # 切换目录
    os.chdir(git_project_path)
    # 拉取最新配置
    str_tmp = os.popen('git pull')

    cmd_back = str_tmp.read().replace('\n', '')

    print(cmd_back)


def is_update():
    backups = configs['backups']

    t = tuple(backups)

    for temp in t:
        print('key:'+temp+' '+'value:'+backups[temp])


if __name__ == '__main__':
    git_pull()
    is_update()
