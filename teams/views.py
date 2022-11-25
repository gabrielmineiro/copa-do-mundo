from .models import Team
from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
import ipdb


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        return teams