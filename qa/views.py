from pydoc_data.topics import topics
from wsgiref.util import request_uri
from django.shortcuts import render

from qa.models import Answer, Question, Topic

def topic(request):
    print("in home")
    return render(request,"topic.html")

def retireveTopic(request):
    print("inside retrieve topic")
    #topic=Topic.objects.all()
    topic=Topic.objects.filter(topic_level=1)
    print("My topics",topic)
    
    return render(request,'topic.html',{'topic':topic})

def retireveSubTopic(request,topic_name):
    print("inside retireveSubTopi")
    print("topic_name", topic_name)
    topic=Topic.objects.get(topic_name=topic_name)
    subtopics=topic.children.all()
    print("My subtopics",subtopics)
    return render(request,'topic.html',{'topic':subtopics})

def retireveQTopic(request):
    print("inside retrieve topic")
    #topic=Topic.objects.all()
    topic=Topic.objects.all()
    print("My topics",topic)
    return render(request,'topicquestions.html',{'topic':topic})

def questionDetails(request, topic_name):
    print("Displaying the details of the subtopics and the questions.")
    #Retrieving the Subtopics for a given topic
    print("topic_name",topic_name)
    rquestions=Question.objects.all().filter(topics__topic_name=topic_name)
    for question in rquestions:
        print("each question in loop", question)
        ranswer=Answer.objects.all().filter(question__question_text=question)
        print("answer", ranswer)
    #print("answers",ranswers)
    print("questions for that topic",rquestions)

    return render(request,'questions.html',{'questions':rquestions})
