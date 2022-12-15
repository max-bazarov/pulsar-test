import io
import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from products.models import Product
from rest_framework import serializers

FILE_UPLOAD_DIR = settings.MEDIA_ROOT


class ImageProcessing(serializers.Field):
    '''Convert image to webp format and saves it to media.'''

    def to_representation(self, value):
        return value.url

    def to_internal_value(self, data):
        try:
            name, extension = str(data).split('.')
        except ValueError:
            raise serializers.ValidationError('Invalid image format')
        if extension not in ['jpg', 'png']:
            raise serializers.ValidationError('Unsupported image extension')

        image = Image.open(data)
        imgstr = io.BytesIO()
        image.save(imgstr, format='WEBP')

        image = InMemoryUploadedFile(
            imgstr,
            None,
            f'{name}.webp',
            'image/webp',
            imgstr.getbuffer().nbytes,
            None)

        default_storage.save(f'images/{image.name}', image)

        return data


class ImageSerializer(serializers.Serializer):
    path = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    def get_path(self, obj):
        path = obj.url
        path = path.split('.')[0]
        return path

    def get_formats(self, obj):
        formats = [
            filename.split('.')[1] for filename
            in os.listdir(FILE_UPLOAD_DIR+'images/')
            if obj.name.split('/')[1].split('.')[0] in filename
        ]
        return formats


class ProductPostSerializer(serializers.ModelSerializer):
    image = ImageProcessing()

    class Meta:
        model = Product
        fields = '__all__'


class ProductGetSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Product
        fields = '__all__'
