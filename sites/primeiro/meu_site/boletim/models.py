from django.db import models


class MateriasSeries(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class MateriaAluno(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Series(models.Model):
    materias = models.ForeignKey(to=MateriasSeries, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Materias(models.Model):
    series = models.ForeignKey(to=MateriasSeries, on_delete=models.CASCADE)
    alunos = models.ForeignKey(to=MateriaAluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    nota = models.IntegerField()

    def __str__(self):
        return self.nome


class Alunos(models.Model):
    materias = models.ForeignKey(to=MateriaAluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
