from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.urls import reverse

from .forms import UserCreateForm
from .models import *

def registrationPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreateForm()

        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'elearningapp/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user= authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'elearningapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    updates = Update.objects.all()
    context = {
        'updates':updates,
    }
    return render(request, 'elearningapp/dashboard.html',context)


@login_required(login_url='login')
def lessons(request):
    return render(request, 'elearningapp/lessons.html')


@login_required(login_url='login')   
def contact(request):
    if request.method == "POST":
        message = request.POST['message']

        send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['chloehonours@gmail.com'],
        fail_silently= False)
    return render(request, 'elearningapp/contact.html')

    
@login_required(login_url='login')   
def update(request,pk):
    update = Update.objects.get(id=pk)
    context = {'update':update}
    return render(request, 'elearningapp/update.html', context)

@login_required(login_url='login')   
def student(request,pk):
    student = Student.objects.get(id=pk)
    return render(request, 'elearningapp/student.html')

@login_required(login_url='login')
def resources(request):
    resources = Resource.objects.all()
    context = {
        'resources':resources,
    }
    return render(request, 'elearningapp/resources.html', context)

#quizzes views
@login_required(login_url='login')    
def tests(request):
    all_quiz_list = Quiz.objects.all()
    context = {
        'all_quiz_list':all_quiz_list,
    }
    return render(request, 'elearningapp/tests.html', context)

def single_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    num_of_questions = len(quiz.question_set.all())

    if num_of_questions == 0:
        quiz.delete()
        all_quiz_list = Quiz.objects.all()
        context = {
            'all_quiz_list': all_quiz_list,
        }
        return render(request, 'elearningapp/tests.html', context)

    quiz.num_of_questions = num_of_questions
    quiz.save()

    request.session["num_correct"] = 0
    request.session["num_incorrect"] = 0

    context = {
        'quiz': quiz,
        'num_of_questions': num_of_questions,
    }
    return render(request, 'elearningapp/single_quiz.html', context)

def single_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    current_question = quiz.question_set.get(question_num=question_id)

    next_or_submit = "Next"
    last_question_check = False
    if question_id == (len(quiz.question_set.all())):
        check_last_question = True
        next_or_submit = "Submit"

    next_question_id = question_id+1

    all_selections = current_question.selection_set.all()

    context = {
        'current_question': current_question,
        'all_selections': all_selections,
        'quiz': quiz,
        'next_question_id': next_question_id,
        'last_question_check': last_question_check,
        'next_or_submit': next_or_submit
    }
    return render(request, 'elearningapp/single_question.html', context)

def select(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    current_question = quiz.question_set.get(question_num=question_id)

    next_or_submit = "Next"
    if question_id == (len(quiz.question_set.all())):
        next_or_submit = "Submit"

    try:
        selection_selected = current_question.selection_set.get(pk=request.POST['selection'])
    except (KeyError, Selection.DoesNotExist):
        return render(request, 'elearningapp/single_question.html', {
            'quiz': quiz,
            'current_question': current_question,
            'error_message': "Please select an answer",
            'next_or_submit': next_or_submit,
        })
    else:

        correct_answer = current_question.selection_set.get(correct=True)

        if selection_selected == correct_answer:
            print("CORRECT")
            request.session["num_correct"] += 1
        else:
            print("INCORRECT")
            request.session["num_incorrect"] += 1

        if question_id == (len(quiz.question_set.all())):
            return HttpResponseRedirect(reverse('results', args=(quiz.id,)))
        else :
            return HttpResponseRedirect(reverse('single_question', args=(quiz.id, question_id+1,)))
            
def results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    num_correct = request.session["num_correct"]
    num_incorrect = request.session["num_incorrect"]

    total_questions = num_correct+num_incorrect

    # formats accuracy as % with no decimal digits
    accuracy = num_correct/(total_questions)

    accuracy_over_75 = False
    if accuracy >= .75:
        accuracy_over_75 = True

    accuracy_imp = "{:.0%}".format(accuracy)

    context = {
        'num_correct': num_correct,
        'num_incorrect': num_incorrect,
        'accuracy_over_75': accuracy_over_75,
        'accuracy_imp': accuracy_imp,
        'total_questions': total_questions,
        'quiz': quiz,
    }
    return render(request, 'elearningapp/results.html', context)

#individual lessons
#lesson 1   
def lesson1x1(request):
    return render(request, 'elearningapp/lesson1/1-1.html')

def lesson1x2(request):
    return render(request, 'elearningapp/lesson1/1-2.html')

def lesson1x3(request):
    return render(request, 'elearningapp/lesson1/1-3.html')

def lesson1x4(request):
    return render(request, 'elearningapp/lesson1/1-4.html')

def lesson1x5(request):
    return render(request, 'elearningapp/lesson1/1-5.html')


#lesson 2
@login_required(login_url='login')    
def lesson2x1(request):
    return render(request, 'elearningapp/lesson2/2-1.html')

@login_required(login_url='login')    
def lesson2x2(request):
    return render(request, 'elearningapp/lesson2/2-2.html')

@login_required(login_url='login')    
def lesson2x3(request):
    return render(request, 'elearningapp/lesson2/2-3.html')

@login_required(login_url='login')    
def lesson2x4(request):
    return render(request, 'elearningapp/lesson2/2-4.html')

@login_required(login_url='login')    
def lesson2x5(request):
    return render(request, 'elearningapp/lesson2/2-5.html')

@login_required(login_url='login')    
def lesson2x6(request):
    return render(request, 'elearningapp/lesson2/2-6.html')

@login_required(login_url='login')    
def lesson2x7(request):
    return render(request, 'elearningapp/lesson2/2-7.html')

@login_required(login_url='login')    
def lesson2x8(request):
    return render(request, 'elearningapp/lesson2/2-8.html')

@login_required(login_url='login')    
def lesson2x9(request):
    return render(request, 'elearningapp/lesson2/2-9.html')

@login_required(login_url='login')    
def lesson2x10(request):
    return render(request, 'elearningapp/lesson2/2-10.html')
 
#lesson 3
@login_required(login_url="login")
def lesson3x1(request):
    return render(request, 'elearningapp/lesson3/3-1.html')

@login_required(login_url='login')    
def lesson3x2(request):
    return render(request, 'elearningapp/lesson3/3-2.html')

@login_required(login_url='login')    
def lesson3x3(request):
    return render(request, 'elearningapp/lesson3/3-3.html')

@login_required(login_url='login')    
def lesson3x4(request):
    return render(request, 'elearningapp/lesson3/3-4.html')

@login_required(login_url='login')    
def lesson3x5(request):
    return render(request, 'elearningapp/lesson3/3-5.html')

@login_required(login_url='login')    
def lesson3x6(request):
    return render(request, 'elearningapp/lesson3/3-6.html')

@login_required(login_url='login')    
def lesson3x7(request):
    return render(request, 'elearningapp/lesson3/3-7.html')

@login_required(login_url='login')    
def lesson3x8(request):
    return render(request, 'elearningapp/lesson3/3-8.html')



#lesson 4
@login_required(login_url="login")
def lesson4x1(request):
    return render(request, 'elearningapp/lesson4/4-1.html')

@login_required(login_url='login')    
def lesson4x2(request):
    return render(request, 'elearningapp/lesson4/4-2.html')

@login_required(login_url='login')    
def lesson4x3(request):
    return render(request, 'elearningapp/lesson4/4-3.html')

@login_required(login_url='login')    
def lesson4x4(request):
    return render(request, 'elearningapp/lesson4/4-4.html')

@login_required(login_url='login')    
def lesson4x5(request):
    return render(request, 'elearningapp/lesson4/4-5.html')

@login_required(login_url='login')    
def lesson4x6(request):
    return render(request, 'elearningapp/lesson4/4-6.html')

@login_required(login_url='login')    
def lesson4x7(request):
    return render(request, 'elearningapp/lesson4/4-7.html')

@login_required(login_url='login')    
def lesson4x8(request):
    return render(request, 'elearningapp/lesson4/4-8.html')

@login_required(login_url='login')    
def lesson4x9(request):
    return render(request, 'elearningapp/lesson4/4-9.html')

@login_required(login_url='login')    
def lesson4x10(request):
    return render(request, 'elearningapp/lesson4/4-10.html')


#lesson 5
@login_required(login_url="login")
def lesson5x1(request):
    return render(request, 'elearningapp/lesson5/5-1.html')

@login_required(login_url='login')    
def lesson5x2(request):
    return render(request, 'elearningapp/lesson5/5-2.html')

@login_required(login_url='login')    
def lesson5x3(request):
    return render(request, 'elearningapp/lesson5/5-3.html')

@login_required(login_url='login')    
def lesson5x4(request):
    return render(request, 'elearningapp/lesson5/5-4.html')

@login_required(login_url='login')    
def lesson5x5(request):
    return render(request, 'elearningapp/lesson5/5-5.html')

@login_required(login_url='login')    
def lesson5x6(request):
    return render(request, 'elearningapp/lesson5/5-6.html')

@login_required(login_url='login')    
def lesson5x7(request):
    return render(request, 'elearningapp/lesson5/5-7.html')

@login_required(login_url='login')    
def lesson5x8(request):
    return render(request, 'elearningapp/lesson5/5-8.html')


#lesson 6
@login_required(login_url="login")
def lesson6x1(request):
    return render(request, 'elearningapp/lesson6/6-1.html')


#lesson 7
@login_required(login_url="login")
def lesson7x1(request):
    return render(request, 'elearningapp/lesson7/7-1.html')


#lesson 8
@login_required(login_url="login")
def lesson8x1(request):
    return render(request, 'elearningapp/lesson8/8-1.html')

    
#lesson 9
@login_required(login_url="login")
def lesson9x1(request):
    return render(request, 'elearningapp/lesson9/9-1.html')

