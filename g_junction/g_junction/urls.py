from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('login_auth.api.urls')),
    path('account/', include('accounts.urls'))
]
