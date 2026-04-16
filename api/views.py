
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CityFilter

class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class = CityFilter
    def get(self,request,*args, **kwargs):
        return self.list(request, *args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args, **kwargs)

class UDRStudentAPI(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
     queryset = Student.objects.all()
     serializer_class= StudentSerializer

     def get(self,request,*args, **kwargs):
         return self.retrieve(request,*args, **kwargs)
     def put(self,request,*args, **kwargs):
         return self.update(request,*args, **kwargs)
     def delete(self,request,*args, **kwargs):
         return self.destroy(request, *args, **kwargs)
    

