from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.index, name="home"),
   path('books', views.bookList, name="books"),
   path('readers', views.readers, name="readers"),
   path('library', views.readersList, name="library"),
   path('addBook', views.addBook, name="addBook"),
   path('editBook/<int:id>', views.editBook, name="editBook"),
   path('editBookf/<int:id>', views.editBookf, name="editBookf"),
   path('deleteBook/<int:id>', views.deleteBook, name="deleteBook"),

   path('addReader', views.addReader, name="addReader"),
   path('editReader/<int:id>', views.editReader, name="editReader"),
   path('editReaderf/<int:id>', views.editReaderf, name="editReaderf"),
   path('deleteReader/<int:id>', views.deleteReader, name="deleteReader"),
   path('issueBook', views.issueBook, name="issueBook"),
   path('returnBook', views.returnBook, name="returnBook"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)