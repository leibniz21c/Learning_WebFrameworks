from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'myapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_list = question.answer_set.all()
    context = {'question':question, 'answer_list':answer_list}
    return render(request, 'myapp/question_detail.html', context)