from django.views.generic import TemplateView, ListView

from models import NewsCategory, News, Article

class NewsListView(ListView):
	template_name = 'news_list.html'
	context_object_name = 'news_list'
	paginate_by = 7

	def get_params(self, **kwargs):
		params = self.request.GET
		return params

	def get_current_category(self, **kwargs):
		params = self.get_params()

		try:
			current_category = NewsCategory.objects.filter(pk=params['category'])[0]
		except:
			current_category = None

		return current_category

	def get_context_data(self, **kwargs):
		context = super(NewsListView, self).get_context_data(**kwargs)
		params = self.get_params()
		context['current_category'] = self.get_current_category
		context['news_category_list'] = NewsCategory.objects.all()
		try:
			context['current_page'] = int(params['page'])
		except :
			context['current_page'] = 1
		return context

	def get_queryset(self, **kwargs):
		current_category = self.get_current_category()

		if current_category:
			qs = current_category.news_set.filter(is_published=True)
		else:
			qs = News.objects.filter(is_published=True)

		return qs



class ArticleListView(ListView):
	template_name = 'article_list.html'
	context_object_name = 'article_list'
	paginate_by = 5

	def get_queryset(self, **kwargs):
		qs = Article.objects.filter(is_published=True)
		return qs

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