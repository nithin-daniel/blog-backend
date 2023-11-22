from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
# Create your views here.
class Sample(APIView):

     def get(self, request, format=None):
        get_post = Blog.objects.all()
        return Response(get_post)