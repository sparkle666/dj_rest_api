from django.contrib import admin
from django.urls import path, include
from core.views import PostAPIView
from rest_framework.authtoken.views import obtain_auth_token #A view used to return auth token for auth users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', PostAPIView.as_view(), name = "index"),
    path('api-token/', obtain_auth_token, name ="obtain-token"),
    path('rest-auth/', include('rest_auth.urls')),
]
