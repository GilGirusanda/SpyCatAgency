from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cat, Mission
from .serializers import CatSerializer, MissionSerializer, TargetSerializer
from rest_framework import status

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        cat_id = request.data.get('cat_id')
        cat = Cat.objects.get(id=cat_id)
        if mission.complete:
            return Response({"error": "Cannot assign a cat to a completed mission."}, status=status.HTTP_400_BAD_REQUEST)
        mission.cat = cat
        mission.save()
        return Response(MissionSerializer(mission).data)

    @action(detail=True, methods=['post'])
    def complete_target(self, request, pk=None):
        mission = self.get_object()
        target_id = request.data.get('target_id')
        target = mission.targets.get(id=target_id)
        if mission.complete:
            return Response({"error": "Mission is already complete."}, status=status.HTTP_400_BAD_REQUEST)
        target.complete = True
        target.save()
        return Response(TargetSerializer(target).data)
