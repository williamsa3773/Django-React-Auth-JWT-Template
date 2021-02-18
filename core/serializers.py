from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class UserSerializerWithToken(serializer.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializer.CharField(write_only=True)

    def get_token(self, obi):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obi)
        token =jwt_encode_handler(payload)
        return get_token

    def create(self, validated_data):
        password = vailidated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')
