from django.db import models

# Create your models here.

class New(models.Model):
    class Meta:
        db_table = "News"

    img_field = models.TextField()
    title = models.CharField(max_length=100)
    new_text = models.TextField()
    published_date = models.DateField(auto_now_add=True)


class Teacher(models.Model):
    class Meta:
        db_table = "Teachers"

    img_field = models.TextField()
    full_name = models.CharField(max_length=100)
    short_about = models.TextField()
    consultation = models.TextField()
    subject_list = {}



