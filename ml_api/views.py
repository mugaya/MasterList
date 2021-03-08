from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404

from ml_main.models import MasterList
from ml_setup.models import ListGeneral
from .serializers import (
    SearchSerializer, SettingsSerializer, FacilitySerializer)


class SettingsViewSet(generics.ListAPIView):
    permission_classes = []
    serializer_class = SettingsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned values to a given prameter.
        """
        queryset = ListGeneral.objects.all()
        field_name = self.request.query_params.get(
            'field_name', 'regulation_status_id')
        if field_name is not None:
            queryset = queryset.filter(field_name=field_name)
        return queryset


class SearchListView(APIView):
    """
    View to list all Master Lists in the system.

    * Requires token authentication for other use cases.
    * Only authenticated users are able to access this view or RO.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = MasterList.objects.all()
        # Get params and this query to be converted to a vector search
        name = request.GET.get('name')
        approval_status = request.GET.get('approval_status')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if approval_status:
            queryset = queryset.filter(approval_status=approval_status)
        adraw = int(request.GET.get('draw', 1))
        serializer = SearchSerializer(queryset, many=True)
        content = serializer.data
        results = {'draw': adraw, 'recordsFiltered': 10,
                   'recordsTotal': 10, 'data': content}
        return Response(results)


class FacilityViewSet(viewsets.ViewSet):
    """
    This will handle all actions for the Master List

    """
    queryset = MasterList.objects.all()
    serializer_class = FacilitySerializer

    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, format=None):
        content = {
            'status': 'Listing not supported'
        }
        return Response(content)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        facility = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(facility)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data,
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
