from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.views import APIView

from .serializers import GroupSerializers


# from rest_framework.mixins import ListModelMixin

@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({"message": "hello World"})


class GroupsListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    # def get(self, request: Request) -> Response:
    #     groups = Group.objects.all()
    # data = [group.name for group in groups]
    # serialized = GroupSerializers(groups, many=True)
    # return Response({"groups": data})
    # return Response({"groups": serialized.data})
