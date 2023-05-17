import os
import re
import json
import shutil


ALLURE_PLUS_DIR = "report/allure_report/"


def get_dirname():
    try:
        history_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
        if os.path.exists(history_file):
            with open(history_file) as f:
                li = eval(f.read())
            # 根据构建次数进行排序，从大到小
            li.sort(key=lambda x: x['buildOrder'], reverse=True)
            # 返回下一次的构建次数，所以要在排序后的历史数据中的buildOrder+1
            return li[0]["buildOrder"]+1, li
        else:
            # 首次进行生成报告，肯定会进到这一步，先创建history.json,然后返回构建次数1（代表首次）
            with open(history_file, "w") as f:
                pass
            return 1, None
    except Exception as e:
        print(e)


def update_trend_data(dirname, allure_url, old_data: list):
    """
    dirname：构建次数
    old_data：备份的数据
    update_trend_data(get_dirname())
    """
    try:
        WIDGETS_DIR = os.path.join(ALLURE_PLUS_DIR, f"{str(dirname)}/widgets")
        # 读取最新生成的history-trend.json数据
        with open(os.path.join(WIDGETS_DIR, "history-trend.json")) as f:
            data = f.read()

        new_data = eval(data)
        if old_data is not None:
            new_data[0]["buildOrder"] = old_data[0]["buildOrder"]+1
        else:
            old_data = []
            new_data[0]["buildOrder"] = 1
        # 给最新生成的数据添加reportUrl key，reportUrl要根据自己的实际情况更改
        new_data[0]["reportUrl"] = f"{allure_url}{dirname}/index.html"
        # 把最新的数据，插入到备份数据列表首位
        old_data.insert(0, new_data[0])
        allure_file = getfilename(ALLURE_PLUS_DIR)
        # 兼容删除allure_report头部文件
        if allure_file is None:
            num = 1
        else:
            num = allure_file[0]
        # 把所有生成的报告中的history-trend.json都更新成新备份的数据old_data，这样的话，点击历史趋势图就可以实现新老报告切换
        for i in range(int(num), dirname+1):
            with open(os.path.join(ALLURE_PLUS_DIR, f"{str(i)}/widgets/history-trend.json"), "w+") as f:
                f.write(json.dumps(old_data))
        # 把数据备份到history.json
        hostory_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
        with open(hostory_file, "w+") as f:
            f.write(json.dumps(old_data))
        return old_data, new_data[0]["reportUrl"]
    except Exception as e:
        print(e)


# 将元素中的数字转换为int后再排序
def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s


# 将元素中的字符串和数字分割开
def str2int(v_str):
    return [tryint(sub_str) for sub_str in re.split('([0-9]+)', v_str)]


# 以分割后的list为单位进行排序
def sort_humanly(v_list):
    return sorted(v_list, key=str2int)


# 获取当前目录下所有的文件夹名字
def getfilename(filename):
    for root, dirs, files in os.walk(filename):
        array = dirs
        if array:
            human_sort_list = sort_humanly(array)
            return human_sort_list


def w_file(filepath, text):
    with open(filepath, 'w') as wf:
        wf.write("var text = " + "\"{}\";".format(text))


def revise_js(filename, url, filename_js):
    """
    @param filename: 待排序文件夹路径
    @param url: allure访问的链接
    @param filename_js: 要修改的文件路径
    """
    file_name = getfilename(filename)
    new_url = url + file_name[-1]
    w_file(filename_js, new_url)


def del_file(filepath):
    """
    清空某一目录下的所有文件
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def del_folder(filepath, quantity):
    """
    删除report/allure_report/路径下的文件（最早的部分）
    :param filepath: 路径
    :param quantity: 文件保留数量
    """
    human_sort_list = getfilename(filepath)
    if human_sort_list is None:
        pass
    elif len(human_sort_list) > quantity:
        num = len(human_sort_list) - quantity
        li = human_sort_list[:num]
        for i in li:
            file = os.path.join(filepath, f"{str(i)}")
            shutil.rmtree(file)
    else:
        pass


def del_history(filepath):
    """
    根据文件夹名称删除对应的history.json记录
    :param filepath: 路径
    """
    try:
        human_sort_list = getfilename(filepath)
        if human_sort_list is not None:
            _, old_data = get_dirname()
            data = []
            for i in old_data:
                if str(i.setdefault('buildOrder', 0)) in human_sort_list:
                    data.append(i)
            # 把数据备份到history.json
            history_file = os.path.join(ALLURE_PLUS_DIR, "history.json")
            with open(history_file, "w+") as f:
                f.write(json.dumps(data))
        else:
            pass

    except Exception as e:
        print(e)
