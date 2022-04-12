from base import BaseClass
from bs4 import BeautifulSoup
from common.replace_all import replace_all


class ProfileExtractor(BaseClass):
    def __init__(self, html, user_id: str = None, selector: dict = None) -> None:
        super().__init__()
        self.uid = user_id
        self.soup = BeautifulSoup(html, 'lxml')
        if not selector:
            self.selector = {
                "name": "head > title:nth-child(1)",
                "education": "#education",
                "work": "#work",
                "placelive": "#living",
                "contact_info": "#contact-info",
                "basic_info": "#basic-info",
                "relationship": "#relationship",
                "nicknames": "#nicknames",
                "year_overviews": "#year-overview",
                "quote": "#quote",
                "bio": "#bio",
                "checkin": None,
                "sport": None,
                "music": None,
                "television": None,
                "books": None,
                "app": None,
                "likes": None,
                "backup_info": None,
                "contents": None
            }
        else:
            self.selector = selector
        self.data = {}

    def _get_attrs(self, attrs):
        self.log.info(f"Getting {attrs} for {self.uid}")
        selector = self.selector.get(attrs)
        self.log.info(f"selector: {selector}")
        try:
            data_container = self.soup.select(selector)[0].text
            data_container = data_container.replace('/n', '')
            data_container = data_container.splitlines()
            data_container = [i + ' ' for i in data_container if i]
            return data_container
        except BaseException as e:
            self.log.error(e)
            return None

    def process_data(self, attrs):
        replacer = {
            "Nơi từng sống": "",
            "Tỉnh/Thành phố hiện tại": "",
            "Quê quán": "",
            "Thông tin cơ bản": "",
            "Ngôn ngữ": "",
            "language": "",
            "Các tên khác": "",
            "Biệt danh": "",
            "Mối quan hệ": "",
            "Other names": "",
            "Nickname": "",
            "Relationship": "",
            "Favourite Quotes": "",
            "Places lived": "",
            "Home town": "",
            "Basic info": "",
            "Facebook": "",
            "Contact Info": "",
            "Current town/city": ""
        }
        field = self._get_attrs(attrs)
        if not field:
            return field
        field = [replace_all(replacer, i) for i in field]
        field = [i for i in field if i]
        field = list(set(field))
        if len(field) == 1 and isinstance(field, list):
            if attrs == 'contact_info' and 'facebook.com' not in field[0]:
                return f'https://www.facebook.com/{field[0]}'
            return field[0]

        return field

    def extract(self) -> dict:
        self.data['name'] = self.process_data('name')
        self.data['placelive'] = self.process_data('placelive')
        self.data['education'] = self.process_data('education')
        self.data['basic_info'] = self.process_data('basic_info')
        self.data['nicknames'] = self.process_data('nicknames')
        self.data['relationship'] = self.process_data('relationship')
        self.data['bio'] = self.process_data('bio')
        self.data['contact_info'] = self.process_data('contact_info')
        self.data['year_overviews'] = self.process_data('year_overviews')
        self.data['quote'] = self.process_data('quote')

        return self.data

def main():
    path = 'resources/sample html/sample3.html'
    f = open(path, 'r')
    html = f.read()
    extractor = ProfileExtractor(html=html)
    print(extractor.extract())

if __name__ == '__main__':
    main()