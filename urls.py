from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.conf import settings

from apps.urls import urlpatterns as apps_urlpatterns

from apps.views import index, InstructionsView
from apps.reviews.views import ReviewIndexView, ReviewListView, MoreReviewsView, ReviewFormView
from apps.capabilities.views import CapabilityListView 
from apps.messages.views import OrderFormView, OrderThanksView, \
                                PartnersView, PartnersDoctorsFormView, PartnersDrugstoresFormView, \
                                PatientsView, PatientsQFormView, PatientsSchoolFormView
from apps.publications.views import ArticleListView, ArticleView, NewsListView, NewsView, PublicationListView, PublicationView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
	(r'^admin/crop/(?P<app_name>\w+)/(?P<model_name>\w+)/(?P<id>\d+)/$', 'views.crop_image_view'),
     #Redactor
    (r'^upload_img/$', 'views.upload_img'),
    (r'^upload_file/$', 'views.upload_file'),
    # index
    (r'^$', index), 
    # reviews
    url(r'^reviews/$', ReviewIndexView.as_view(), name='reviews_url'),
    url(r'^reviews/patients/$', ReviewListView.as_view(), {'reviewer_type':'patient'}, name='patients_reviews_url'),
    url(r'^reviews/doctors/$', ReviewListView.as_view(), {'reviewer_type':'doctor'}, name='doctors_reviews_url'),
    (r'^reviews/patients/more/$', MoreReviewsView.as_view(), {'reviewer_type':'patient'}),
    (r'^reviews/doctors/more/$', MoreReviewsView.as_view(), {'reviewer_type':'doctor'}),
    (r'^reviews/patients/form/$', ReviewFormView.as_view()),
    (r'^reviews/doctors/form/$', ReviewFormView.as_view()),
    # capabilities
    url(r'^capabilities/$', CapabilityListView.as_view(), name='capabilities_url'),
    # order form
    url(r'^order/$', OrderFormView.as_view(), name='order_url'),
    url(r'^thanks/$', OrderThanksView.as_view()),
    # instructions
    url(r'^instructions/$', InstructionsView.as_view(), name='instructions_url'),
    # for_patients
    url(r'^for_patients/$', PatientsView.as_view(), name='patients_url'),
    url(r'^for_patients/q_form/$', PatientsQFormView.as_view(), name='patients_q_url'),
    url(r'^for_patients/school_form/$', PatientsSchoolFormView.as_view(), name='patients_school_url'),
    # for_partners
    url(r'^for_partners/$', PartnersView.as_view(), name='partners_url'),
    url(r'^for_partners/doctors_form/$', PartnersDoctorsFormView.as_view(), name='partners_doctors_url'),
    url(r'^for_partners/clinics_form/$', PartnersDrugstoresFormView.as_view(), name='partners_drugstores_url'),
    # publications
    url(r'^newsboard/$', NewsListView.as_view(), name='news_list_url'),
    url(r'^articles/$', ArticleListView.as_view(), name='article_list_url'),
    url(r'^publications/$', PublicationListView.as_view(), name='publication_list_url'),
    url(r'^publications/(?P<id>\d)/$', PublicationView.as_view(), name='publication_url'),
    url(r'^newslist/(?P<id>\d)/$', NewsView.as_view(), name='single_news_url'),
    url(r'^articles/(?P<id>\d)/$', ArticleView.as_view(), name='article_url'),
)

urlpatterns += apps_urlpatterns
