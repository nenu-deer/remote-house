import os
import requests
from bs4 import BeautifulSoup
#检查用户访问权限
def check_permisson(user_id):
    if user_id == "admin":
        return True
    else:
        return False


#检查文件路径是否有效和可访问
def check_path(file_path):
    if os.path.exists(file_path) and os.access(file_path,os.R_OK):
        return True
    else:
        return False


#下载网页内容并保存到本地
def download_webpage(url,file_path):
    #发送请求
    response = requests.get(url)
    #检查响应状态码
    if response.status_code == 200:
        #获取响应内容
        page_content = response.content
        #将内容保存到指定路径
        with open (file_path,"wb")as file:
            file.write(page_content)
        print("网页下载成功到",file_path)
    else:
        print("false,状态码",response.status_code)
