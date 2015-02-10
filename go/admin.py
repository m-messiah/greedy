from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from go.models import Game, Task, Code, Player
from django.utils import timezone


class CodeInline(admin.TabularInline):
    model = Code
    readonly_fields = ('post_time',)
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ("game", "num", "desc")
    fields = ["game", "num", "desc", "duration",
              "hint1", "hint1_time",
              "hint2", "hint2_time",
              "is_bonus"]

    inlines = [CodeInline]
    list_filter = ["game"]
    search_fields = ["game"]


class GameAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "start", "active")
    fieldsets = [
        (None,          {'fields': ["name", "author"]}),
        (_('Information'), {'fields': ["legend", "tools",
                                       "pretask", "start", "end"]})
    ]

    class ActiveGameFilter(admin.SimpleListFilter):
        # Translators: It's title of filter
        title = _('Active')
        parameter_name = 'active'

        def lookups(self, request, model_admin):
            # Translators: Filter parameters
            return (
                ('1', _('active')),
                ('0', _('finished'))
            )

        def queryset(self, request, queryset):
            if self.value() == '1':
                return queryset.filter(end__gte=timezone.now())
            if self.value() == '0':
                return queryset.filter(end__lte=timezone.now())

    list_filter = ["start", "author", ActiveGameFilter]
    search_fields = ["name", "legend"]


admin.site.register(Game, GameAdmin)
admin.site.register(Task, TaskAdmin)


class UserInline(admin.StackedInline):
    model = Player
    can_delete = False
    verbose_name_plural = 'Игрок'


class UserAdmin(UserAdmin):
    inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)