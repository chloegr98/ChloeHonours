from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registrationPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    

    path('', views.home, name="home"),
    path('lessons/', views.lessons, name="lessons"),
    path('contact/', views.contact, name="contact"),
    path('resources/', views.resources, name="resources"),
    path('update/<str:pk>/', views.update, name="update"),
    path('student/<str:pk>/', views.student, name="student"),

    path('quiz/', views.tests, name="quiz"),
    path('<int:quiz_id>/', views.single_quiz, name='single_quiz'),
    path('<int:quiz_id>/<int:question_id>/', views.single_question, name='single_question'),
    path('<int:quiz_id>/<int:question_id>/select/', views.select, name='select'),
    path('<int:quiz_id>/results/', views.results, name='results'),

    #indiviudual lessons
    #lesson 1
    path('1-1/', views.lesson1x1, name="1x1"),
    path('1-2/', views.lesson1x2, name="1x2"),
    path('1-3/', views.lesson1x3, name="1x3"),
    path('1-4/', views.lesson1x4, name="1x4"),
    path('1-5/', views.lesson1x5, name="1x5"),

    #lesson 2
    path('2-1/', views.lesson2x1, name="2x1"),
    path('2-2/', views.lesson2x2, name="2x2"),
    path('2-3/', views.lesson2x3, name="2x3"),
    path('2-4/', views.lesson2x4, name="2x4"),
    path('2-5/', views.lesson2x5, name="2x5"),
    path('2-6/', views.lesson2x6, name="2x6"),
    path('2-7/', views.lesson2x7, name="2x7"),
    path('2-8/', views.lesson2x8, name="2x8"),
    path('2-9/', views.lesson2x9, name="2x9"),
    path('2-10/', views.lesson2x10, name="2x10"),


    #lesson 3
    path('3-1/', views.lesson3x1, name="3x1"),
    path('3-2/', views.lesson3x2, name="3x2"),
    path('3-3/', views.lesson3x3, name="3x3"),
    path('3-4/', views.lesson3x4, name="3x4"),
    path('3-5/', views.lesson3x5, name="3x5"),
    path('3-6/', views.lesson3x6, name="3x6"),
    path('3-7/', views.lesson3x7, name="3x7"),
    path('3-8/', views.lesson3x8, name="3x8"),

    #lesson 4
    path('4-1/', views.lesson4x1, name="4x1"),
    path('4-2/', views.lesson4x2, name="4x2"),
    path('4-3/', views.lesson4x3, name="4x3"),
    path('4-4/', views.lesson4x4, name="4x4"),
    path('4-5/', views.lesson4x5, name="4x5"),
    path('4-6/', views.lesson4x6, name="4x6"),
    path('4-7/', views.lesson4x7, name="4x7"),
    path('4-8/', views.lesson4x8, name="4x8"),
    path('4-9/', views.lesson4x9, name="4x9"),
    path('4-10/', views.lesson4x10, name="4x10"),

    #lesson 5
    path('5-1/', views.lesson5x1, name="5x1"),
    path('5-2/', views.lesson5x2, name="5x2"),
    path('5-3/', views.lesson5x3, name="5x3"),
    path('5-4/', views.lesson5x4, name="5x4"),
    path('5-5/', views.lesson5x5, name="5x5"),
    path('5-6/', views.lesson5x6, name="5x6"),
    path('5-7/', views.lesson5x7, name="5x7"),
    path('5-8/', views.lesson5x8, name="5x8"),

    #lesson 6
    path('6-1/', views.lesson6x1, name="6x1"),

    #lesson 7
    path('7-1/', views.lesson7x1, name="7x1"),

    #lesson 8
    path('8-1/', views.lesson8x1, name="8x1"),

    #lesson 9
    path('9-1/', views.lesson9x1, name="9x1"),

    

]