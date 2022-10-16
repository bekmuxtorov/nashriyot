from django.db import models
from .const import Const
from ckeditor.fields import RichTextField

# Create your models here.
class Articles(models.Model):
    categories = Const.categories
    title = models.CharField(max_length=100, verbose_name='Sarlavha:')
    image = models.ImageField()
    category = models.CharField(
        max_length=35,
        choices=categories,
        default=1
    )
    date = models.DateTimeField(auto_now_add=True)
    body = RichTextField(verbose_name='Maqola matni:')
    blog_view = models.IntegerField(default=0)

    def get_absolute_url(self):
            return f"/article/{self.id}"
    
    def get_category(self):
        return dict(Articles.categories)[self.category]

    def get_date(self):
        now = self.date
        date_time = now.strftime("%d/%m/%Y")
        return date_time

    def __str__(self):
        return self.title
    


