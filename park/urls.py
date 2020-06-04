from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
# from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('load_form', views.load_form),
    path('add', views.add),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search',views.search),
    path('employees',views.EmployeeList.as_view()),
    path('r^(.*)$)', views.welcome),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = views.handler404
# handler500 = views.handler500
