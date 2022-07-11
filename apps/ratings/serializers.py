from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rater=serializers.SerializerMethodField(read_only=True)
    agent=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    # when defining a serializer method field below has to be "get_" then variable defined above
    def get_rater(self, obj):
        # "rater" below comes from models.py which link to user
        return obj.rater.username
    
    def get_agent(self, obj):
        # "agent" comes from models.py which links to the profiles app "user" which links to the django's user auth model via "get_user_model()"
        return obj.agent.user.username
