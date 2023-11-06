from django.forms import ModelForm
from .models import photoPost
class PhotoPostForm(ModelForm):
    class Meta:

        model = photoPost
        fields =['category','title','comment','image1','image2']