import requests
from bs4 import BeautifulSoup
import pprint
import json

def dwonload_all_htmls():
    """
    下载html数据
    :return:
    """
    htmls = []
    for idx in range(24):

        url = f"    {idx+1}"    //网页地址,f是格式化
        print("craw html",url)
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls

def parse_single_html(html):
    soup = BeautifulSoup(html,'html.parser')
    articles = soup.find_all('article')
    datas = []
    for articles in articles :
        title_node = (
            article
            .find("h2",class_="entry-title")
            .find("a")
        )
        title = title_node.get_text()
        link = title_node["href"]
        tag_nodes = (
            article
            .find("footer",class_="entry-footer")
            .find("span",class_="tags-links")
            .find all("a")
        )
        datas.append(
            {"title":title,"link":link,"tags":tags}
        )
    return datas
