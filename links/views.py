from django.views.generic import ListView, DetailView
from .models import Link, Vote, UserProfile
from django.contrib.auth import get_user_model

class LinkListView(ListView):
	model = Link
	queryset = Link.with_votes.all()

class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = "username"
	template_name = "user_detail.html"

	def get_object(self, queryset=None): # overwrites the built-in get_object function. Make sure it always retrieves the user profile before creating the get_object
		user = super(UserProfileDetailView, self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user
