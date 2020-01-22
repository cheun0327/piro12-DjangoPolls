from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from polls.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index")

def detail(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # question=get_object_or_404(Question, pk=question_id)로 대체가능

    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

## 여기부분 잘 이해안댐...
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context={   # 템플릿에서 쓰이는 변수명과 파이썬 객체를 연결하는 딕셔너리 값
        'latest_question_list' : latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)