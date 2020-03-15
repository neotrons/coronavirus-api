from django.urls import re_path, include

app_name = 'api_v1'

urlpatterns = [
    re_path('cases/', include('apps.cases.api.urls')),
]
