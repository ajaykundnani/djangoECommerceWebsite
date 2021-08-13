from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

class UserList(APIView):
    def get(self,request):
        model = Users.objects.all()
        serializer  = UsersSerializers(model,many = True)
        return Response(serializer.data) 

    def post(self,request):
        serializer = UsersSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



class UserModify(APIView):
    def get(self,request,id):
        model = Users.objects.get(id=id)
        serializer  = UsersSerializers(model)
        return Response(serializer.data) 

    def put(self,request,id):
        model = Users.objects.get(id=id)
        serializer = UsersSerializers(model,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        duser = Users.objects.get(id = id)
        duser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)