from django.db import models

# Create your models here.


class Perguntas(models.Model):
    texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField('data publicada')

    def __str__(self):
        return self.texto


class Respostas(models.Model):
    texto = models.CharField(max_length=200)
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
