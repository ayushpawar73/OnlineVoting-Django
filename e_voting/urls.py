from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
      path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('acc/', include('account.urls')),
    path('administrator/', include('administrator.urls')),
    path('voting/', include('voting.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
