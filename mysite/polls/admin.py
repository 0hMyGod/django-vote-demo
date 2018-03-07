from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    search_fields = ('id', 'question_text', 'pub_date')
    list_filter = ['pub_date']
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
