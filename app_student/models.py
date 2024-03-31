from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 80, verbose_name =' Student name')
    age = models.IntegerField(verbose_name = 'Student age')
    mark_1 = models.IntegerField(verbose_name ='mathematical analysis' )
    mark_2 = models.IntegerField(verbose_name ='physics' )
    mark_3 = models.IntegerField(verbose_name ='geometry' )
    mark_4 = models.IntegerField(verbose_name ='artificial intelligence' )
    mark_5 = models.IntegerField(verbose_name = 'philosophy')
    mark_6 = models.IntegerField(verbose_name = 'algebra')
    mark_7 = models.IntegerField(verbose_name = 'history')
    image = models.ImageField(verbose_name='Student image',upload_to='students')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'student'
        verbose_name = 'Students list'
        ordering = ('id',)

