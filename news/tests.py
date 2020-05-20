from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.Kevin = Editor(first_name = 'Kevin', last_name = 'Munene', email = 'muneneeekev@gmail.com')
        self.Kevin.save()
    #testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.Kevin,Editor))

    #test save method
    def test_save_method(self):
        self.Kevin.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0)


    def test_delete_method(self):
        self.Kevin.delete_editor()
        editorz = Editor.objects.all()
        self.assertTrue(len(editorz) < 1)


class ArticleTestClass(TestCase):

    def setUp(self):
        self.Kevin= Editor(first_name = 'Kevin', last_name = 'Munene', email ='muneneeekev@gmail.com')
        self.Kevin.save_editor()

        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'This is a random test post',editor = self.Kevin)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)


    def teardown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()


    def test_get_news_today(self):
        todays_news = Article.todays_news()
        self.assertTrue(len(todays_news)>0)


    def test_get_news_by_date(self):
        test_date = '2020-04-18'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
        