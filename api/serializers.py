from rest_framework import serializers 
from .models import CustomUser , Book  , ReadingList , ReadingListEntry


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user 
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = '__all__'

class ReadingListEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListEntry
        fields = ['book', 'order']

class ReadingListSerializer(serializers.ModelSerializer):
    entries = ReadingListEntrySerializer(many=True, read_only=True)

    class Meta:
        model = ReadingList
        fields = ['id', 'user', 'entries']

class ReadingListAddBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    order = serializers.IntegerField()

class ReadingListRemoveBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()



