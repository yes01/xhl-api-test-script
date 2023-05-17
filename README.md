# xhl-api-test-script

小火龙平台 - API 测试脚本


**多进程、多线程使用方法**

```markdown
介绍：
1、pytest-parallel支持多进程、多线程--不支持allure报告生成、html报告log打印无序
2、pytest-xdist只支持多进程--完美兼容allure、html报告生成
使用：
pytest-parallel--指定运行的进程数，默认为1（-w）、指定运行的线程数（-tc）、参数为数字则为指定运行进程数或线程数
pytest-xdist--指定运行的进程数（-n），参数为auto，会自动检测系统的CPU数目、参数为数字则为指定运行进程数
```

**框架使用方法**

***1、拉取代码至本地，在根目录下创建 project 文件夹用户存放测试用例以及用例所需参数***
```markdown
project
├── __init__.py
├── modules       存放用例参数
└── testcase      存放测试用例
```

***2、安装框架所需要的依赖库***
```sh
pip install -r requirements.txt
```

***3、配置allure环境***
```sh
ps:配置jdk环境
MAC:
1.下载allure.tgz包
curl -O https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.22.0/allure-commandline-2.22.0.tgz
2.配置环境变量
tar -zxvf allure-commandline-2.22.0.tgz
# 进入解压后的文件夹
cd allure-2.22.0/bin 
# 配置环境变量
vi ~/.bash_profile
PATH="/Users/xxx/allure-2.22.0/bin:${PATH}"
export PATH
source ~/.bash_profile
window:
1.下载allure.zip包
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.22.0/allure-commandline-2.22.0.zip
2.将压缩包解压后,复制安装包到想安装的路径
3.配置环境变量:将allure的bin目录所在路径添加到系统环境变量path中
4.验证是否配置成功:cmd进入命令行窗口,输入allure进行验证
```

***4、执行框架命令***
```sh
python run.py -h  # 查看命令用法

usage: run.py [-h] [--file FILE [FILE ...] | --stories STORIES | --features
              FEATURES | --severities SEVERITIES] [--env ENV] [--report]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE [FILE ...], -f FILE [FILE ...]
                        需要测试的文件
  --stories STORIES, -s STORIES
                        需要测试的用例名(stories)
  --features FEATURES, -fe FEATURES
                        需要测试的用例名(features)
  --severities SEVERITIES, -se SEVERITIES
                        需要测试的用例名(severities)
  --env ENV, -e ENV     需要测试的环境名称(e.g. dev)
  --report, -r          是否需要发送报告

allure报告查看:
  allure open -p 9000 report/allure_report

```

