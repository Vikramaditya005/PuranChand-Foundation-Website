from django.urls import path
from . import views
from .views import (
    HomeView, ContactView, AboutUsView,
    GalleryView, TeamView, MediaCentreView,
    NewsListView, NewsDetailView, AllProjectsView,
    ProjectDetailView, UserSignupView, volunteer_submit,
    dashboard, VideoListView, ReviewListView, UserLoginView,
    launch_campaign, PodcastListView, NewspaperCuttingListView, EventPhotoListView,
)
from django.contrib.auth.views import LogoutView

# This app_name variable is what namespaces your URLs.
# You MUST use this namespace when referencing URLs in your templates and views.
app_name = 'foundation_app'

urlpatterns = [
    # General Pages
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('team/', TeamView.as_view(), name='team'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('contact/', ContactView.as_view(), name='contact'),
    path("volunteer/", views.volunteer_page, name="volunteer_page"),

    # Dashboard and User Actions
    path("dashboard/", dashboard, name="dashboard"),
    path('launch-campaign/', launch_campaign, name='launch_campaign'),
    path('volunteer/submit/', volunteer_submit, name='volunteer_submit'),

    # Media Centre and News
    path('media-centre/', MediaCentreView.as_view(), name='media_centre'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path("podcasts/", PodcastListView.as_view(), name="podcast_list"),
    path("videos/", VideoListView.as_view(), name="video_list"),
    path("newspaper-cuttings/", NewspaperCuttingListView.as_view(), name="newspaper_cuttings"),
    path("event-photos/", EventPhotoListView.as_view(), name="event_photos"),
    

    # Projects and Reviews
    path('projects/', AllProjectsView.as_view(), name='all_projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    
    # User Authentication
    path('signup/', UserSignupView.as_view(), name='signup'),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", views.custom_logout, name="logout"),
]
