from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class Task(models.Model) :

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    priority_list = [('HP', 'High Priority'),
                     ('MP', 'Medium Priority'),
                     ('LP', 'Low Priority')]

    deadline = models.TimeField()
    priority = models.CharField(max_length=2, choices=priority_list, default='MP')


    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title

# Create your models here.
