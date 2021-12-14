from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#     path('/heros', include('rest_framework.urls', namespace='rest_framework')),
from .views import HeroView

urlpatterns = [
    path('heros/', HeroView.as_view(), name='heroView'),
]
