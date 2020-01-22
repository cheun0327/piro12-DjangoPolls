from django.contrib import admin
from .models import Question

admin.site.register(Question)       # admin사이트에서 poll app을 변경가능하도록 만들기
