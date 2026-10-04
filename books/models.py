from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Book(models.Model):
    title=models.CharField( max_length=50)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    isbn=models.CharField(max_length=13,unique=True)
    description=models.CharField(blank=True,default="")
    cover_url=models.URLField(blank=True,default="")
    published_year=models.PositiveBigIntegerField(null=True,blank=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        ordering=["-created_at"]
        indexes=[
            models.Index(fields=["author"]),
            models.Index(fields=["title"])
        ]

    def __str__(self):
        return f"{self.title} - {self.author} "

    