# xhl-api-test-script

小火龙平台 - API 测试脚本

```

**多进程、多线程使用方法**

***
介绍：
1、pytest-parallel支持多进程、多线程--不支持allure报告生成、html报告log打印无序
2、pytest-xdist只支持多进程--完美兼容allure、html报告生成
使用：
pytest-parallel--指定运行的进程数，默认为1（-w）、指定运行的线程数（-tc）、参数为数字则为指定运行进程数或线程数
pytest-xdist--指定运行的进程数（-n），参数为auto，会自动检测系统的CPU数目、参数为数字则为指定运行进程数
***

