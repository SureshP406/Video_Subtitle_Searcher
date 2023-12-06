from django import forms

from django.utils.translation import gettext_lazy as _

from .models import Video


class VideoUploadForm(forms.ModelForm):
                  class Meta:
                          model = Video
                          fields = ['video_file']



class VideoSearchForm(forms.ModelForm):
        class Meta:
                model = Video     
                fields = ['subtitle,' , 'start_time' , 'end_time']

                widgets = {
                        'subtitles': TextInput(attrs={'class' : 'required form_control', 'placeholder' : 'Subtitles'}), 
                }    

                error_messages = {
                        
                        'subtitles' : {'required' : _("Subtitles field is required."),},
                }                  