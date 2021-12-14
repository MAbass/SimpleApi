from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from rest_framework.views import APIView

from SimpleApiApp.models import Hero
from SimpleApiApp.serializers import HeroSerializer


class HeroView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        heros = Hero.objects.all()
        heroSerializer = HeroSerializer(heros, many=True)
        return Response({"heros": heroSerializer.data})

    def post(self, request):
        heroSerializer = HeroSerializer(data=request.data)
        if heroSerializer.is_valid():
            heroSerializer.save()
            return Response({"status": "success", "data": heroSerializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": heroSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
