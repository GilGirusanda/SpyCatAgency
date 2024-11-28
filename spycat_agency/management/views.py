from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Cat, Mission, Target
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
        
        try:
            cat = Cat.objects.get(id=cat_id)
        except Cat.DoesNotExist:
            return Response({"error": "Cat not found."}, status=status.HTTP_404_NOT_FOUND)

        if mission.complete:
            return Response({"error": "Cannot assign a cat to a completed mission."}, status=status.HTTP_400_BAD_REQUEST)

        # if any cat took particular mission, then the other cat cannot take that busy mission.
        if mission.cat:
            return Response({
                "error": "This mission already has a cat assigned."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # if the cat is already involved into any active mission, he cannot take new one.
        if Mission.objects.filter(cat=cat, complete=False).exists():
            return Response({
                "error": "This cat is already assigned to another mission in progress."
            })

        mission.cat = cat
        mission.save()
        return Response(MissionSerializer(mission).data)
    
    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat:
            return Response({
                "error": "This mission is assigned to a cat and can\'t be removed."
            }, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class UpdateTargetStatusView(APIView):
    """ 
    View to update the target's status of completeness
    """
    def patch(self, request, pk=None, action=None):
        
        try:
            target = Target.objects.get(id=pk)
        except Target.DoesNotExist:
            return Response({"error": "Target not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if target.complete:
            return Response({"error": "Target is already complete."}, status=status.HTTP_400_BAD_REQUEST)

        target.complete = True
        target.save()

        # Check if all targets in the mission are complete
        if all(t.complete for t in target.mission.targets.all()):
            target.mission.complete = True
            target.mission.save()

        return Response({
            "target": TargetSerializer(target).data,
            "mission_completed": target.mission.complete
        }, status=status.HTTP_200_OK)

class UpdateTargetNotesView(APIView):
    """
    View to update the notes of a target.
    """
    def patch(self, request, pk=None):
        try:
            target = Target.objects.get(id=pk)
        except Target.DoesNotExist:
            return Response({"error": "Target not found."}, status=status.HTTP_404_NOT_FOUND)

        notes = request.data.get('notes')

        if target.complete:
            return Response({"error": "Can\'t update a completed target."}, status=status.HTTP_400_BAD_REQUEST)

        if notes is not None:
            target.notes = notes
            target.save()
        else:
            return Response({
                "error": "Notes cannot be empty",
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "target": TargetSerializer(target).data,
        }, status=status.HTTP_200_OK)