from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API - Casos confirmados en el mundo de COVID-19",
      default_version='v1',
      description="""
      API rest de reporte de casos confirmados en el mundo de coronavirus COVID-19 presentados en 
      [Coronavirus COVID-19 Global Cases by the Center for Systems Science and Engineering (CSSE) 
      at Johns Hopkins University (JHU)](
      https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
      
      __Autor:__ [Jose Ramirez](https://www.linkedin.com/in/jcramireztello/)
      
      _esta api utiliza la especificacion [JSON:API](https://jsonapi.org/)_
      """,
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
