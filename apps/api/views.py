from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     return HttpResponse("Hello, world. You're at the api index.")


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.name for q in latest_question_list])
#     return HttpResponse(output)

# from django.template import loader
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template("api/index.html")
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))

# 更新视图函数,使用django.shortcuts的render,直接省略HttpResponse
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "api/index.html", context)

# 符合django视图的格式，含有HttpResponse才能被django识别为视图函数
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
