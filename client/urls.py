from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('about/',views.about,name='about'),
    path('video/',views.video,name='video'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('video1/',views.video1,name='video1'),
    path('video2/',views.video2,name='video2'),
    path('video3/',views.video3,name='video3'),
    path('video4/',views.video4,name='video4'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path ('book/',views.book,name='book'),
    path('view/',views.view,name='view'),
    path('update/<int:id>',views.update,name='update'),
    path('booking/',views.booking,name='booking'),
    path('update_client/<int:id>',views.update_client,name='update_client'),


    path('testing',views.testing,name='testing'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('testing/update/<int:id>',views.update_hall,name='testing_update')

]