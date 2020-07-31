from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Materias)
admin.site.register(models.Series)
admin.site.register(models.Alunos)
admin.site.register(models.MateriaAluno)
admin.site.register(models.MateriasSeries)
