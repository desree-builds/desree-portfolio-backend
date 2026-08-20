from django.db import models

# Create your models here.
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Language'),
        ('framework', 'Framework'),
        ('tool', 'Tool'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name