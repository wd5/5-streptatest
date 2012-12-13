from django.views.generic import TemplateView, ListView

from models import NewsCategory, News, Article

class NewsListView(TemplateView):
	template_name = 'news_list.html'

	def get_context_data(self, **kwargs):
		context = super(NewsListView, self).get_context_data(**kwargs)
		params = self.request.GET

		try:
			current_category = NewsCategory.objects.filter(pk=params['category'])[0]
		except:
			current_category = None

		if current_category:				
			news_list = current_category.news_set.filter(is_published=True)
		else:
			news_list = News.objects.filter(is_published=True)

		context['current_category'] = current_category
		context['news_category_list'] = NewsCategory.objects.all()
		context['news_list'] = news_list
		return context


class ArticleListView(TemplateView):
	template_name = 'article_list.html'

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)
		context['article_list'] = Article.objects.filter(is_published=True)
		return context

class ArticleView(TemplateView):
	template_name = 'article.html'

	def get_context_data(self, **kwargs):
		context = super(ArticleView, self).get_context_data(**kwargs)

		try:
			context['article'] = Article.objects.get(pk=kwargs['id'])
		except:
			context['article'] = None

		return context

class NewsView(TemplateView):
	template_name = 'news_item.html'

	def get_context_data(self, **kwargs):
		context = super(NewsView, self).get_context_data(**kwargs)

		try:
			context['article'] = News.objects.get(pk=kwargs['id'])
		except:
			context['article'] = None

		return context