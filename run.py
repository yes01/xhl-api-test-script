import time
import platform
import argparse
import pytest
from utils.allure import *

parser = argparse.ArgumentParser()
ALLURE_PATH = os.path.join("report/allure_results", str(int(time.time())))
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("--file", "-f", help="需要测试的文件", nargs="+")
group.add_argument("--stories", "-s", help="需要测试的用例名(stories)")
group.add_argument("--features", "-fe", help="需要测试的用例名(features)")
group.add_argument("--severities", "-se", help="需要测试的用例名(severities)")
parser.add_argument("--env", "-e", help="需要测试的环境名称(e.g. dev)")
parser.add_argument("--workers", "-w", help="指定运行的进程数，默认为1，windows系统中只能为1(pytest-parallel)")
parser.add_argument("--n", "-n", help="参数为auto，会自动检测系统的CPU数目.如果参数为数字，则指定运行测试的处理器进程(pytest-xdist)")
parser.add_argument("--threads", "-tc", help="指定运行的线程数(pytest-parallel)")
# parser.add_argument("--report", "-r", help="是否需要发送报告", action="store_true")
# parser.add_argument("--one_click_test", "-o", help="一键测试sha", default=False)
# report_list = ["--alluredir={}".format(ALLURE_PATH), "--html=report.html", "--self-contained-html"]
report_list = ["--alluredir={}".format(ALLURE_PATH), "--html=report.html", "--self-contained-html", "--capture=sys"]

args = parser.parse_args()
if args.file:
    test_file = args.file
elif args.stories:
    test_file = ["-s", "-q", "--allure-stories=" + args.stories]
elif args.features:
    test_file = ["-s", "--allure-features=" + args.features]
elif args.severities:
    test_file = ["-s", "--allure-severities=" + args.severities]
else:
    test_file = []
if args.n:
    concurrency = ["-n=" + args.n]
elif args.workers:
    concurrency = ["--workers=" + args.workers]
elif args.threads:
    concurrency = ["--tests-per-worker=" + args.threads]
else:
    concurrency = []
self_args = test_file + report_list + concurrency

if __name__ == '__main__':
    system_name = platform.system()
    del_folder("./report/allure_report/", 10)
    del_history("./report/allure_report/")
    pytest.main(self_args)
    buildOrder, old_data = get_dirname()
    allure_report = os.path.join(ALLURE_PLUS_DIR, str(buildOrder))
    allure_url = ""
    allure_url_local = "http://localhost:9000/"
    if system_name == 'Linux':
        url = allure_url
        rep = '/data/webapp/allure-2.14.0/bin//allure generate {0} -o {1} --clean'.format(ALLURE_PATH, allure_report)
    else:
        url = allure_url_local
        rep = 'allure generate {0} -o {1} --clean'.format(ALLURE_PATH, allure_report)
    os.system(rep)
    # 执行完毕后再调用update_trend_data()
    all_data, reportUrl = update_trend_data(buildOrder, url, old_data)
    revise_js("./report/allure_report", str(url), "./report/allure_report/txt.js")
    del_file("./report/allure_results")
