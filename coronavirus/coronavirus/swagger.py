from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="REPORTE DE CORONAVIRUS API",
      default_version='v1',
      description="API rest para el reporte de coronavirus"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
