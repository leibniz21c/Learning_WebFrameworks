from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse


# Create your views here.

# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   
#    # 그냥 이렇게 심플하게 템플릿을 로드해서 이렇게 해주면됨.
#    template = loader.get_template('polls/index.html')
#    # context를 통해서 데이터를 전달함.
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

def index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   context = {'latest_question_list': latest_question_list }
   return render(request, 'polls/index.html', context)


# 기존의 http 404 에러 발생 방식
# def detail(request, question_id):
#     try :
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist :
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question':question})

# shortcut으로 http 404 발생 방식
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) 
    # 위의 polls/detail.html은 서버의 파일 경로임을 꼭 생각하자. 뷰에는 파일 경로만
    
    


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html'), {
            'question': question,
            'error_message' : "You didn't select a choice.",
        }
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
