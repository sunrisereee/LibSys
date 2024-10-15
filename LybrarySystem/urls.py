from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.index, name="home"),
   path('books', views.books_list, name="books"),
   path('readers', views.readers, name="readers"),
   path('library', views.library, name="library"),
   path('addBook', views.addBook),
   path('editBook', views.editBook),
   path('deleteBook', views.deleteBook),

   path('addReader', views.addReader),
   path('editReader', views.editReader),
   path('deleteReader', views.deleteReader),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)