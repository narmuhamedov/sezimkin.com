from django.utils.safestring import mark_safe
from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(models.Slider, PostAdmin)


class PostAdminLogo(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 200px;">')


admin.site.register(models.Logo, PostAdminLogo)


admin.site.register(models.AboutME)


class PostAdminphoto(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image_about.url}" style="max-height: 200px;">'
        )


admin.site.register(models.AboutMEPhoto, PostAdminphoto)

admin.site.register(models.Target)
admin.site.register(models.Contact)
