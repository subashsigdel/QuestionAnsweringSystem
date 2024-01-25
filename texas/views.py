# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AskQuestionForm, AnswerQuestionForm
from .models import YourModel, Answer

def home(request):
    form = AskQuestionForm()
    answer_form = AnswerQuestionForm()

    if request.method == 'POST':
        if 'question' in request.POST:
            form = AskQuestionForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'answer' in request.POST:
            answer_form = AnswerQuestionForm(request.POST)
            if answer_form.is_valid():
                question_id = request.POST.get('question_id')
                question = get_object_or_404(YourModel, id=question_id)
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.save()

    recent_questions = YourModel.objects.all()

    return render(request, 'base.html', {'form': form, 'answer_form': answer_form, 'recent_questions': recent_questions})

def ask_question(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AskQuestionForm()

    return render(request, 'ask.html', {'form': form})



def answer_question(request, question_id):
    question = get_object_or_404(YourModel, id=question_id)

    if request.method == 'POST':
        answer_form = AnswerQuestionForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('home')
    else:
        answer_form = AnswerQuestionForm(initial={'question_id': question.id})

    return render(request, 'base.html', {'answer_form': answer_form, 'question': question})

