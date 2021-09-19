# pip install kivy
# pip install certifi

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
import certifi as cfi
import random

Builder.load_file('design.kv')

class NewsScreen(Screen):
    def get_news(self):
        api_key = "6c28b118e84a488c85beef5bfc7217ea"
        main_url = "https://newsapi.org/v2/top-headlines?country=cn&apiKey=" + api_key
        self.news = UrlRequest(main_url, on_success=self.news_list, ca_file=cfi.where(), verify=True)

    def news_list(self, req, *args):
        all_news = self.news.result
        article = all_news["articles"]
        news_articles = []
        for ar in article:
            news_articles.append(ar["title"])

        final_news_artical = news_articles[random.randint(0, 15)]
        self.ids.newss.text = final_news_artical
        print(final_news_artical)

class mainWidget(ScreenManager):
    pass

class main(App):
    def build(self):
        return mainWidget()

if __name__ == "__main__":
    main().run()