from django import forms
from .models import UserProfile
from .models import Link

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ("user",)

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		exclude = ("submitter", "rank_score") #we exclude those bc we already know who the submitter is (request.user), and we compute the score separately
