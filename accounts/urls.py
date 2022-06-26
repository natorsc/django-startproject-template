from django.urls import path

from .views import SignUpView, profile

app_name = 'accounts'
urlpatterns = [
    path(route='profile/', view=profile, name='profile'),
    path(route='signup/', view=SignUpView.as_view(), name='signup'),
]
