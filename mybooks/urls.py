from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ebooks.views import *
from mybooks import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('book/<int:pk>', book_detail, name='book_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='ebooks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='ebooks/logout.html'), name='logout'),
    path('add_book/', login_required(book_create), name='add_book'),
    path('delete_book/<int:pk>/', login_required(book_delete), name='delete_book'),
    path('edit_book/<int:pk>/', login_required(book_update), name='edit_book'),
    path('book/<int:pk>/download', download_book, name='download_book')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
