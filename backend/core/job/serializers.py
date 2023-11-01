from .models import *
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'
        
class CandidatesAppliedSerializer(serializers.ModelSerializer):
    # ino vase tlow test kon:
    job=JobSerializer()
 
    class Meta:
        model=CandidatesApplied
        fields=('user','resume','appliedAt','job')