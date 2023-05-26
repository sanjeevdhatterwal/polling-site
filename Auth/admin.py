from django.contrib import admin
# admin admin
# pwd 1234!@#$
# Register your models here.
from main import models
admin.site.register([
    models.Question,
    models.Choice,
    models.Answer
]
)