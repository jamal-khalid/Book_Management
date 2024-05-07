from django.shortcuts import render , get_object_or_404
from rest_framework import generics , permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny  , IsAuthenticated
from rest_framework.views import APIView 
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer, ReadingListSerializer , ReadingListEntrySerializer , BookSerializer , ReadingListAddBookSerializer,ReadingListRemoveBookSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Book , ReadingList , ReadingListEntry , CustomUser

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username , "*"*10)
        print(password ,"$"*10)

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        print(user , "*"*20)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user 
    

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    # permission_classes = [IsOwnerOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsOwnerOrReadOnly]

class ReadingListCreateAPIView(generics.CreateAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]

class ReadingListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]


class ReadingListAddBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        reading_list = get_object_or_404(ReadingList, pk=pk)
        serializer = ReadingListAddBookSerializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            order = serializer.validated_data['order']
            book = get_object_or_404(Book, pk=book_id)
            reading_list.add_book(book, order)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadingListRemoveBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        reading_list = get_object_or_404(ReadingList, pk=pk)
        serializer = ReadingListRemoveBookSerializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            book = get_object_or_404(Book, pk=book_id)
            reading_list.books.remove(book)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



