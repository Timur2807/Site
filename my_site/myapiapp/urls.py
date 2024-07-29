from django.urls import path, include
from .views import hello_world_view, GroupsListView

app_name = "myapiapp"

urlpatterns = [
    # path("api/", include("rest_framework.urls")),
    path("hello/", hello_world_view, name="myapiapp"),
    path("groups/", GroupsListView.as_view(), name="groups"),
]
