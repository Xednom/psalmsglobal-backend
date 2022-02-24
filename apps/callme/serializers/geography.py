from rest_framework import serializers

from apps.callme.models import State, County


__all__ = ("stateSerializer", "CountySerializer")


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("name",)


class CountySerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(
        slug_field="name", queryset=State.objects.all()
    )

    class Meta:
        model = County
        fields = ("name", "state")
