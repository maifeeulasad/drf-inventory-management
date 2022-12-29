from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


class Profileview(APIView):
    def post(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)