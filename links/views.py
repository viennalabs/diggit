from django.views.generic import ListView, DetailView
from .models import Link, Vote, UserProfile
from .forms import UserProfileForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse #does a reverse lookup of the url

class LinkListView(ListView):
	model = Link
	queryset = Link.with_votes.all()
	paginate_by = 10

class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = "username"
	template_name = "user_detail.html"

	def get_object(self, queryset=None): # overwrites the built-in get_object function. Make sure it always retrieves the user profile before creating the get_object
		user = super(UserProfileDetailView, self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user

class UserProfileEditView(UpdateView):
	model = UserProfile
	form_class = UserProfileForm
	template_name = "edit_profile.html"

	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0] #first is just the user objects
	
	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})
