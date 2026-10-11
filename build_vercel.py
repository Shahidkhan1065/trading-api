"""Vercel build: migrate (+ seed when empty) so the API has content after deploy."""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model
from cms.models import PageSection


def main() -> None:
    print('Running migrations...')
    call_command('migrate', interactive=False, run_syncdb=True)

    if not PageSection.objects.exists():
        print('Seeding CMS content...')
        call_command('seed_content')
    else:
        print('CMS content already present — skip seed.')

    User = get_user_model()
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@alealamitrading.com')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Created superuser: {username}')
    else:
        print(f'Superuser {username} already exists.')

    print('Vercel build complete.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'Build warning: {exc}', file=sys.stderr)
        # Do not fail the whole deploy if DB is temporarily unavailable at build time
        # (migrations will need to be run once DATABASE_URL is configured).
        if os.environ.get('DATABASE_URL'):
            raise
