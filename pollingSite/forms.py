from django import forms

class createClassForm(forms.Form):
    class_name = forms.CharField(max_length=20)
    class_id = forms.CharField(max_length=20)

class createPollForm(forms.Form):
    new_poll_name = forms.CharField(max_length=20)
    possible_answers = forms.IntegerField()
    correct_answer = forms.IntegerField()
    #start_time = forms.DateTimeField()
    #end_time = forms.DateTimeField()