from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from .models import Question, Answer
from .forms import AskForm, AnswerForm
#, SignupForm, LoginForm

#from functions import pagepag
#from django.contrib.auth import login,authenticate, logout

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def allq(request):
#    all_questions = Question.objects.all()
    all_questions = Question.objects.order_by('-id')
    page = request.GET.get('page', 1)
#    limit = request.GET.get('limit', 10)
#    [paginator,page] = pagepag(request, questions, url)
    paginator = Paginator(all_questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
#    try:
#        page = paginator.page(page)
#    except EmptyPage:
#        page = paginator.page(paginator.num_pages) 
#    return HttpResponse('NOK')
    return render(request, 'qa/questions.html', {
        'question' : all_questions,
        'paginator': paginator, 'page': page,
        'user': request.user,
         })

def popular(request):
    pops = Question.objects.order_by('-rating')
    page = request.GET.get('page', 1)
    paginator = Paginator(pops, 10)
    paginator.baseurl = '/?page='
#    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/questions.html', {
        'question' : pops,
        'paginator': paginator, 'page': page,
         })
   
def show_question(request, q_id):
    try:
        id_question = int(q_id)
    except ValueError:
        raise Http404
    try:
        question = Question.objects.get(id = id_question)
#        question = get_object_or_404(Question, pk=q_id)
    except Question.DoesNotExist:
        raise Http404
    answers = models.Answer.objects.filter(question=question)
    return render(request, 'qa/question.html', {
        'question' : question,
#        'answers' :  Answer.objects.filter(id=id_question).order_by('-added_ad')[:],
        'answers' : answers,
#        'newanswer': AnswerForm({'question': int(id_question), 'author': request.user}),
        'title' : question.title,
        'text' : question.text,
        })

def question_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
#        form.author = request.user
        if form.is_valid():
            post = form.save()
            url = post.get_url()
#           return HttpResponseRedirect('/question/123')
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})

#def question_add(request):
#    url = '/question/'
#    if request.method == "POST":
#        if request.POST['author']:
#            author = request.POST['author']
#        else:
#            author = request.user
#        form = AskForm({
#            'title': request.POST['title'],
#            'text': request.POST['text'],
#            'author': author,
#        },)
#        if form.is_valid():
#            url = url + str( form.save() ) + '/'
#        return HttpResponseRedirect(url)
#        return HttpResponseRedirect('/question/123/')
#    form = AskForm({'author': request.user}) 
#    return render(request, 'qa/ask.html',{
#        'form': form,
#    },)

def post_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect('/question/123')
    else:
        form = AnswerForm()
