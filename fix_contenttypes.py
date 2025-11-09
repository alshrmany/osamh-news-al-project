import os
import django
from django.conf import settings

# إعداد إعدادات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osamh_ahmed_al.settings')
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.apps import apps

# إصلاح ContentTypes
def fix_contenttypes():
    try:
        # حذف جميع ContentTypes وإعادة إنشائها
        ContentType.objects.all().delete()

        # إعادة إنشاء ContentTypes لجميع التطبيقات المثبتة
        for app_config in apps.get_app_configs():
            for model in app_config.get_models():
                ContentType.objects.get_or_create(
                    app_label=app_config.label,
                    model=model._meta.model_name,
                )
        print("تم إصلاح ContentTypes بنجاح!")
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    fix_contenttypes()