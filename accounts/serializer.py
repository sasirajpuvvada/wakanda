from rest_framework import serializers
from rest_framework.validators import  ValidationError
from accounts.models import FiliUser
 
 
class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = FiliUser
        fields = ('email', 'title', 'mobile', 'about_me', 'languages', 'password')
    
    def validate(self, attrs):

        email_exists = FiliUser.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("email already exists")
        
        return super().validate(attrs)
    

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
