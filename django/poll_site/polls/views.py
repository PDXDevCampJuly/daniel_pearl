from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from polls.models import Question
from django.http import HttpResponse, Http404

# Lists all the questions in a list
def questions(request):
    # Grab all the questions from the Model Question
    question_list = Question.objects.all()

    # Get the template that we want, which is questions.html
    template = loader.get_template('questions.html')

    # Create ceontext to return with a template, in HTTPResponse
    context = RequestContext(request, {
        'question_list' : question_list,
    })

    # Returns the HTTPResponse with a template that has the context in it
    return HttpResponse(template.render(context))

# Shows the specific text and choices fo a question
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    return render(request, 'detail.html', {'question':question})