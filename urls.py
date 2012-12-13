from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.conf import settings

from apps.urls import urlpatterns as apps_urlpatterns

from apps.views import index, InstructionsView
from apps.reviews.views import ReviewIndexView, ReviewListView, MoreReviewsView, ReviewForm
from apps.capabilities.views import CapabilityListView 
from apps.messages.views import OrderFormView

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
    (r'^reviews/patients/form/$', ReviewForm.as_view(), {'reviewer_type':'patient'}),
    (r'^reviews/doctors/form/$', ReviewForm.as_view(), {'reviewer_type':'doctor'}),
    # capabilities
    url(r'^capabilities/$', CapabilityListView.as_view(), name='capabilities_url'),
    # order form
    url(r'^order/$', OrderFormView.as_view(), name='order_url'),
    # instructions
    url(r'^instructions/$', InstructionsView.as_view(), name='instructions_url'),

)

urlpatterns += apps_urlpatterns
