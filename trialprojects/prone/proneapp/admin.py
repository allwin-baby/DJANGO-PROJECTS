from django.contrib import admin
from proneapp.models import Question,Answer,Option
# Register your models here.

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
