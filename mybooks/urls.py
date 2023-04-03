from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ebooks.views import *
from mybooks import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('book/<int:pk>', book_detail, name='book_detail'),
    path('book/<int:pk>/download', download_book, name='download_book')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
