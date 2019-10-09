from lab_1.news import app, get_response
import unittest
import datetime
from bs4 import BeautifulSoup


class HtmlTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_tittles(self):
        request = get_response("https://yandex.com/news/rubric/politics?from=index")
        self.assertEqual(request.status_code, 200)
        response = self.app.get('/', follow_redirects=True)
        html_page=(BeautifulSoup(response.data, 'html.parser'))
        articles = []
        for title_tag in html_page.find_all('li'):
            articles.append({"tittle": title_tag.text})
        self.assertNotEqual(articles, ['articles'][0]['tittle'])
    if __name__ == "__main__":
        unittest.main()
