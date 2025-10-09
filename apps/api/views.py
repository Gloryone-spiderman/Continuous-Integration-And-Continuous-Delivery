from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render  # 快捷方法render
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.urls import reverse  # reverse() 调用将返回一个这样的字符串"/polls/3/results/"


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     return HttpResponse("Hello, world. You're at the api index.")


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.name for q in latest_question_list])
#     return HttpResponse(output)


# 被淘汰的loader方法
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


#
# # 符合django视图的格式，含有HttpResponse才能被django识别为视图函数
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "api/detail.html", {"question": question})


# 快捷函数get_object_or_404
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "api/detail.html", {"question": question})


def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Exception as e:
        print("sf ", e)
    return render(request,"api/results.html",{"question":question})


# HttpResponseRedirect 重定向方法
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "api/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("api:results", args=(question.id,)))
