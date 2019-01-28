from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hello.serializers import HelloWorldSerializer
from hello.models import HelloWorld
from django.http import HttpResponse
from rest_framework import status

def home(request):
    return HttpResponse("<p>Hello World!</p>")

def errorpage(request):
    return HttpResponse("<p>oops! there's something wrong!</p>")

# Create your views here.
class HelloWorldView(APIView):

    def get(self, request, year=None):
        print("===GET===")
        qry_str = ""

        hello = None
        if len(request.GET)>0 :
            qry_str = request.GET['data1']
        elif year != None :
            qry_str = str(year)
        else :
            print("???")
        # print("======1:::"+qry_str)
        try :
            hello = HelloWorld.objects.get(pk=qry_str)
            # print("======2:::")
        except :
            # print("======3:::")
            hello = HelloWorld('','')
            
        ser = HelloWorldSerializer(hello)
        print(ser)

        return Response(ser.data)

    def post(self, request):
        print("===POST===")
        print(request.data)
        ser = HelloWorldSerializer(data=request.data)
        if ser.is_valid():
            serializer.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        print("===PUT===")
        print(request.data)
        ser = HelloWorldSerializer(data=request.data)
        if ser.is_valid() :
            ser.save()
            return Response(ser.data)
        
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, year):
        print("===DELETE===")
        print(year)
        try :
            hello = HelloWorld.objects.get(pk=year)
            hello.delete()
        except :
            print("有錯喔")
            hello = HelloWorld('no data can be deleted','')
            

        return Response(status=status.HTTP_204_NO_CONTENT)

# class XYZ(APIView):
#     def get(self, request):
#         return Response({'a':'1'})