"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
	path(
		route='',
		view=views.PostsFeedView.as_view(),
		name='feed'
	),
	path(
		route='posts/<str:slug>/',
		view=views.PostDetailView.as_view(),
		name='detail'
	),
	path(
		route='post/new/',
		view=views.CreatePostView.as_view(),
		name='create'
	),
]
