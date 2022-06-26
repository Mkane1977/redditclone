from django.urls import path, include
from . import views
from django.conf import settings
from .views import display_images, home_view
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<uuid:pk>/', views.post_detail, name='post_detail'),
    path('sub/<uuid:pk>/', views.sub_detail, name='sub_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<uuid:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<uuid:pk>/comment/', views.add_comment, name='add_comment_to_post'),
    path('post/<uuid:pk>/comment/<uuid:parent_pk>/', views.add_comment, name='add_reply_to_comment'),
     path('', home_view ),
    path('reddit_images', display_images, name = 'reddit_images'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
   path("accounts/", include("accounts.urls")),
  # path('accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)