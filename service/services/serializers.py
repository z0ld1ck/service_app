from rest_framework import serializers

from services.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return (instance.service.full_price
                - instance.service.full_price * (instance.plan.discount_percent / 100))


    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email', 'price')
