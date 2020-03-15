from rest_framework.routers import DefaultRouter
from .views import CasesViewSet

app_name = 'cases'
router = DefaultRouter()
router.register(r'', CasesViewSet, basename="cases")
urlpatterns = router.urls
