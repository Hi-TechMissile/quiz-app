from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *

def index(request):
    user = request.user
    if user.is_authenticated:
        context = {
            'username': user.username,
            'score': user.score,
            'questions': user.remaining_questions.all(),
            'count': user.remaining_questions.all().count()
        }
        print(user.remaining_questions.all())
        return render(request, "index.html", context=context)

    else:
        return render(request, 'index.html')

@login_required
def question(request, id):
    # q = Question.objects.filter(id=id)
    # print(q)
    user = request.user
    q = Question.objects.get(question_number=id)
    if q not in user.remaining_questions.all():
        return redirect('index')
    context = {
        'name': q.name,
        'question_number': q.question_number,
        'description': q.description,
        'imgpath': q.imgpath
    }
    # print(q)
    return render(request, 'question.html', context=context)

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            context = {
                'error': 'invalid user.'
            }
            print('invalid user.')
            return render(request, 'login.html', context=context)
    
    return render(request, 'login.html')

def Logout(request):
    # logout(request, request.user)
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            context = {
                'error': 'passwords don\'t match'
            }
            return render(request, 'signup.html', context)
        
        all_questions = Question.objects.all()
        # user.remaining_questions.add(all_questions)

        user = User.objects.create_user(username=username, password=password)

        user.remaining_questions.set(all_questions)
        user.save()
        login(request, user)
        return redirect('index')
    
    return render(request, 'signup.html')

@login_required
def check_answer(request):
    if request.method == "POST":
        user = request.user
        question_number = request.POST.get('number')
        print(question_number)
        answer = request.POST.get('answer')

        question = Question.objects.get(question_number=question_number)
        if question in user.remaining_questions.all():
            context = {
                'number': question_number
            }

            if answer == question.answer:
                print("correct.")
                user.score = user.score + 1
                user.save()
                context['message'] = 'accepted'
            
            else:
                print("incorrect.")
                context['message'] = 'rejected'
            
            user.remaining_questions.remove(question)
            user.save()

            return render(request, 'index.html', context)
        
        else:
            context = {
                'error': 'question is already answered'
            }
            return render(request, 'index.html', context)
    return redirect('index')