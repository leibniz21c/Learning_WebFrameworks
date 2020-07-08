from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    """
    Question 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'myapp/question_list.html', context)

def detail(request, question_id):
    """
    Qusetion 목록 상세 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'myapp/question_detail.html', context)

