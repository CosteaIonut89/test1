import os
import selenium
from selenium import webdriver
import time
from datetime import datetime
import pytest
from selenium import webdriver
import urllib3
import warnings
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.options import Options


# Variables for the root path where need to change with you own paths
# Chrome driver root
root_path = r'D:\Python Projects\CheckLeads\testCases\chromedriver.exe'
download_root_path = "C:/Users/coste/Downloads/**/*.docx"

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=root_path)
    return driver

@pytest.fixture(scope="class")
def setup(request):
    global driver_init

    driver_init = webdriver.Chrome(executable_path=root_path)
    request.cls.driver = driver_init
    yield driver_init
    driver_init.close()


@pytest.fixture
def download():
    download_path = download_root_path
    return download_path

def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)



@pytest.hookimpl(hookwrapper=True)
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):

    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        # extra.append(pytest_html.extras.url('E:\Python Projects\StackField\screenshot'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            feature_request = item.funcargs["request"]
            driver = feature_request.getfixturevalue("setup")
            timestamp = datetime.now().strftime('%H-%M-%S')
            img_name = "name" + timestamp + ".png"
            img_path = os.path.join(r'.\screenshot', img_name)
            # img_path = os.path.join("D:\Python Projects\StackField\screenshot", img_name)
            driver.save_screenshot(img_path)
            # extra.append(pytest_html.extras.image('E:\Python Projects\StackField\screenshot' + timestamp + '.png'))

        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.image(img_path))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "Automation report"