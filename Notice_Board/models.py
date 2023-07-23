from django.db import models

# Create your models here.
class Board_list(models.Model):
    todo = models.CharField(max_length=20)
    description = models.TextField()
    important = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}] {self.borad2}'

    # def get_absolute_url(self):
    #     return '/borad/'