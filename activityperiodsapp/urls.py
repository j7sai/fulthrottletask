from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'useractivites/', views.UserListView.as_view())
]