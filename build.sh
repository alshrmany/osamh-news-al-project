#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput

# فقط طبق migrations إذا كانت قاعدة البيانات متاحة
python manage.py migrate || echo "Migration failed, continuing..."