
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class RoleView(APIView):
    def get(self, request):
        roles = []
        for manager in Manager.objects.all():
            roles.append({ "name": manager.first_name, "role": manager.get_role() })
        for intern in Intern.objects.all():
            roles.append({ "name": intern.first_name, "role": intern.get_role() })
        return Response(roles)
