from django.db import models

# Create your models here.
class Site(models.Model):
    УИД = models.CharField(max_length=36, primary_key=True)
    Работа = models.CharField(max_length=150)
    Инициатор = models.CharField(max_length=100)
    ГИП = models.CharField(max_length=100)
    КомментарийГИП = models.CharField(max_length=512)
    Изготовлено = models.DateTimeField()
    def get_queryset(self):
        return Site.objects.all()

    def get_data(self):
        return self.get_queryset()
    class Meta:
        db_table = 'Site'
        managed = False
