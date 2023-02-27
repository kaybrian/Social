from django.urls import path
from . import views

urlpatterns = [
    path('me/',views.ViewProfile.as_view(), name="profile"),
    path('user/<str:pk>/',views.ViewAnotherProfile.as_view(),name="anotheruser")
]

