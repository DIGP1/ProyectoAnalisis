<<<<<<< HEAD

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
=======

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
>>>>>>> adea497916b6fbb42bf4fdedd9214626e0f16cf5
