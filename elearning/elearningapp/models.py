from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.firstname


class Resource(models.Model):
    resource_name = models.CharField(max_length=200, null=True)
    resource_location = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.resource_name

class Update(models.Model):
    update_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    update_text = models.CharField(max_length=1500, null=True)

    def __str__(self):
        return self.update_name



class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)
    quiz_description = models.CharField(max_length=300, null=True)
    num_of_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=200)
    question_num = models.IntegerField(default=0)

    def __str__(self):
        return self.question_name


class Selection(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selection_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.selection_text