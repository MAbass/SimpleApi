from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#     path('/heros', include('rest_framework.urls', namespace='rest_framework')),
from .views import HeroView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('heros/', HeroView.as_view(), name='heroView'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
