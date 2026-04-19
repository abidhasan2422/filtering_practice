
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.filters import SearchFilter

class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends =[SearchFilter]
    # search_fields =['city'] icontains 
    # search_fields =['^city'] # Start letter must match
    search_fields =['=city'] # Exactly match
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
    

