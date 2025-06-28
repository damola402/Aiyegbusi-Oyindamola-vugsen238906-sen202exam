from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class RoleView(APIView):
    def get(self, request):
        roles = {}
        for m in Manager.objects.all():
            roles[m.name] = m.get_role()
        for i in Intern.objects.all():
            roles[i.name] = i.get_role()
        return Response(roles)