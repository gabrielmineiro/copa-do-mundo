from .models import Team
from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
import ipdb


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        
        team_list =[]
        for team in teams:
            team_dict = model_to_dict(team)
            team_list.append(team_dict)
        
        return Response(team_list)
    
    def post(self, request):
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id= team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)
        return Response(team_dict)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(id= team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        

        team.name = request.data.get("name", team.name)
        team.titles = request.data.get("titles", team.titles)
        team.top_scorer = request.data.get("top_scorer", team.top_scorer)
        team.fifa_code = request.data.get("fifa_code", team.fifa_code)
        team.founded_at = request.data.get("founded_at", team.founded_at)

        team.save()

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id= team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



