from rest_framework import serializers

from attendance.models import Circle, Meeting, Member, Participation


class BaseReactModelSerializer(serializers.HyperlinkedModelSerializer):
    key = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        abstract = True
        fields = ('key', 'url')


class SimpleCircleSerializer(BaseReactModelSerializer):

    class Meta:
        model = Circle
        fields = BaseReactModelSerializer.Meta.fields + ('title',)


class CircleSerializer(BaseReactModelSerializer):

    class Meta:
        model = Circle
        fields = BaseReactModelSerializer.Meta.fields + (
            'title', 'start_date', 'description', 'team', 'members')
        extra_kwargs = {'members': {'write_only': True}}


class MemberSerializer(BaseReactModelSerializer):

    class Meta:
        model = Member
        fields = BaseReactModelSerializer.Meta.fields + (
            'first_name',
            'middle_name',
            'last_name',
            'preferred_name',
            'email')


class MeetingSerializer(BaseReactModelSerializer):

    class Meta:
        model = Meeting
        fields = BaseReactModelSerializer.Meta.fields + ('circle', 'date_time')


class MeetingTableSerializer(BaseReactModelSerializer):
    circle_title = serializers.CharField(source='circle', read_only=True)

    class Meta:
        model = Meeting
        fields = BaseReactModelSerializer.Meta.fields + (
            'circle',
            'circle_title',
            'date',
            
        )


class ParticipationSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id', read_only=True)
    member_name = serializers.CharField(source='member.preferred_name',
                                        read_only=True)

    class Meta:
        model = Participation
        fields = ('key', 'meeting', 'member', 'member_name', 'attended')
