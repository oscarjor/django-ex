from django.contrib import admin
from .models import Employer
from .models import Employee
from .models import Task_Status
from .models import Taks
from .models import Event_Type
from .models import Event
from .models import Quote
from .models import Exercise
from .models import Habit
from .models import Motivation
from .models import Message
from .models import Sound
# Register your models here.

admin.site.register(Employer)
admin.site.register(Employee)
admin.site.register(Task_Status)
admin.site.register(Taks)
admin.site.register(Event_Type)
admin.site.register(Event)
admin.site.register(Quote)
admin.site.register(Habit)
admin.site.register(Exercise)
admin.site.register(Motivation)
admin.site.register(Message)
admin.site.register(Sound)