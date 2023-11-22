from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class Sample(APIView):

     def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = "Sample Api for testing"
        return Response(usernames)