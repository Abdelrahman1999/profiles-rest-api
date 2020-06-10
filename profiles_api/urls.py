from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
#register specific viewsets with our router
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #since we used router.register, we do not need 'hello-viewset/' as in the above url
    #and we want to include all urls from this set into the base url called
    path('',include(router.urls))
]
