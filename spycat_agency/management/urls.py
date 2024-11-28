from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, MissionViewSet, UpdateTargetStatusView, UpdateTargetNotesView

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'missions', MissionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/targets/<int:pk>/complete/', UpdateTargetStatusView.as_view(), name='complete-target'),
    path('api/targets/<int:pk>/update-notes/', UpdateTargetNotesView.as_view(), name='update-target-notes')
]
