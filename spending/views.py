from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView

from spending.serializers import UserSerializer,ExpenseSerializer
from spending.models import Expense





# Create your views here.




class SignUpview(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class GetmeView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        instance = User.objects.get(username=auth_user)

        serializer_instance = UserSerializer(instance)

        return Response(data=serializer_instance.data)

class ExpenselistCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instance = Expense.objects.filter(owner = request.user)

        serializer_instance = ExpenseSerializer(instance,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data  = request.data

        serializer_instance = ExpenseSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner = request.user)               ##if using model serializer 

            # cleaned_data = serializer_instance.validated_data

            # instance = Expense.objects.create(**cleaned_data,owner=request.user)

            # serializer_instance = ExpenseSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class ExpenseRetrieveUpdateDeleteView(RetrieveAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [ permissions.IsAuthenticated]

    def get(self,request,pk=None):

        # instance = Expense.objects.get(id=pk)

        instance = get_object_or_404(Expense,id=pk)

        serializer_instance = ExpenseSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        
        instance = get_object_or_404(Expense,id=pk)

        form_data = request.data

        serializer_instance = ExpenseSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        instance.delete()

        return Response(data={"message":"deleted"})









    
        


    









    

