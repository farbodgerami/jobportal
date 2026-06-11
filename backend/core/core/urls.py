 
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView ,TokenObtainPairView,TokenRefreshView
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/',include('job.urls')),
    path('api/account/',include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='tokenverify'),
     path("health/", health),
]
 