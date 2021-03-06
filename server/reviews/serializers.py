from django.contrib.auth import get_user_model

from rest_framework import serializers

from reviews.models import Review, MIN_RATING_VALUE, MAX_RATING_VALUE
from authy.serializers import UserSerializer


User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):

    def validate_rating(self, rating):
        if not MIN_RATING_VALUE <= rating <= MAX_RATING_VALUE:
            raise serializers.ValidationError('Rating value not valid.')

        return rating

    class Meta:
        model = Review
        fields = '__all__'
