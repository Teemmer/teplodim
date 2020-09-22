from django.db import models


class Article(models.Model):
    image = models.ImageField(upload_to='uploads/', default='uploads/empty.png')
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class File(models.Model):
    article = models.ForeignKey(Article, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
