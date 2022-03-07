from django.db import models

class Topic(models.Model):
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    LEVEL4 = 4
    TOPIC_LEVEL_CHOICES = (
        (LEVEL1, "LEVEL1"),
        (LEVEL2, "LEVEL2"),
        (LEVEL3, "LEVEL3"),
        (LEVEL4, "LEVEL4"),
    )
    topic_name=models.CharField(max_length=200)
    children=models.ManyToManyField("self",blank=True, null=True,symmetrical=False,related_name="topic_children")
    topic_level= models.IntegerField(choices=TOPIC_LEVEL_CHOICES,default =1)
    def __str__(self):
        return "%s" % (self.topic_name)

class Question(models.Model):
    question_text=models.CharField(max_length=500)
    topics=models.ManyToManyField(Topic,related_name="topic_questions")
    def __str__(self):
        return "%s" % (self.question_text)

class Answer(models.Model):
    EXCELLENT="E"
    GOOD = "G"
    AVERAGE = "A"
    POOR = "P"
    GRADE_CHOICES=[(EXCELLENT, "excellent"), (GOOD, "good"),(AVERAGE,"average"),(POOR,"poor")]
    answer=models.CharField(max_length=1000)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, default=EXCELLENT)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return "%s: %s (%s)" % (self.question,self.answer,self.grade)

