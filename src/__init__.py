from download import Downloader
from parse import Parser
from data import Data, json_read

URL = "https://biggeek.ru/catalog/apple-iphone"
PARAMS = {}
FILE_PATH = "dataset.html"
PARSED_FILE_PATH = "dataset.json"

def process(url, web_page_path=None, data_path=None):

    downloader = Downloader(URL=URL, params=PARAMS, method="GET")
    downloader.get_html()
    downloader.save(FILE_PATH)

    parser = Parser(source=FILE_PATH)
    parser.parse()
    parser.save(PARSED_FILE_PATH)

    data = Data(json_read("dataset.json"))
    print(data.grouping_cheap())
    print(data.grouping_average())
    print(data.grouping_expensive())
    print(data.find_by_color("Black"))


process(URL)
