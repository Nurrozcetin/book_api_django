from rest_framework import serializers
from book_api.models import Book

#objeyi json dataya serialize ediyoruz
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    page_number = serializers.IntegerField()
    publish_date = serializers.DateField()
    stock = serializers.IntegerField()