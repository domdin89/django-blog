from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/detail/<int:id>', views.post_detail, name='post-detail'),
    path('blog/new/', views.new, name='new'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # pragma: nocover
