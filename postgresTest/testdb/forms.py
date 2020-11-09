from django import forms 
from .models import Reportform 
  
  
# creating a form 
class ReportFor(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Reportform 
  
        # specify fields to be used 
        fields = [ 
    "location_1",
    "location_2",
    "discription",
    "date",
    "time",
    "severity",
    "casue",
    "action",
    "type_env",
    "type_inj",
    "type_prop",
    "submitted",
    "reported_by",

        ] 