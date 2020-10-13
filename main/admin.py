from django.contrib import admin
import datetime

from .forms import SubRubricForm
from .models import AdvUser, SubRubric, SuperRubric
from .utilities import send_activation_notification


def send_activation_notifications(model_admin, request, queryset):
    for req in queryset:
        if not req.is_activated:
            send_activation_notification(req)
    model_admin.message_user(request, 'Письма с требованиями отправлены')


send_activation_notifications.short_description = 'Отправка писем с требованиями активации'


class NonActivatedFilter(admin.SimpleListFilter):
    title = 'Прошли активацию?'
    parameter_name = 'activate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3 дней'),
            ('week', 'Не прошли более недели'),
        )

    def queryset(self, request, queryset):
        if (val := self.value()) == 'activated':
            return queryset.filter(is_active=True,
                                   is_activated=True)

        elif val == 'threedays':
            d = datetime.datetime.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False,
                                   is_activated=False,
                                   date_joined__date__lt=d)

        elif val == 'week':
            d = datetime.datetime.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False,
                                   is_activated=False,
                                   date_joined__date__lt=d)


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonActivatedFilter,)
    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('send_messages', 'is_active', 'is_activated'),
        ('is_staff', 'is_superuser'),
        ('groups', 'user_permissions'),
        ('last_login', 'date_joined'),
    )
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


admin.site.register(SuperRubric, SuperRubricAdmin)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


admin.site.register(SubRubric, SubRubricAdmin)
