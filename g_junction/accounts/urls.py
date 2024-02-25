from django.urls import path, include
# from .views import Record, Login, Logout

urlpatterns = [
    # path('addUser/', Record.as_view(), name="register"),
    # path('login/', Login.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
    path('auth/', include('accounts.urls'))
]