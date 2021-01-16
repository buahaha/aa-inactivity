# AA Inactivity

This is a player activity monitoring plugin app for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) (AA).

![License](https://img.shields.io/badge/license-GPL-green) ![python](https://img.shields.io/badge/python-3.6-informational) ![django](https://img.shields.io/badge/django-3.1-informational) ![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

## Features

- Notify users inactive for a specified time.

# Installation

## Requirements

This integration needs [Member Audit](https://gitlab.com/ErikKalkoken/aa-memberaudit) and [Secure Groups](https://github.com/pvyParts/allianceauth-secure-groups) to function. Please make sure they are installed before continuing.

## Steps

### Step 1 - Install the Package

Make sure you are in the virtual environment (venv) of your Alliance Auth installation. Then install the newest release from PyPI:

`pip install aa-inactivity`

### Step 2 - Config

Add `inactivity` to your `INSTALLED_APPS`, and add the following task definition:

```python
CELERYBEAT_SCHEDULE['inactivity_check_inactivity'] = {
    'task': 'inactivity.tasks.check_inactivity',
    'schedule': crontab(minute=0, hour=0),
}
```

### Step 3 - Finalize App Installation

Run migrations:

```bash
python manage.py migrate
```

Restart your supervisor services for Auth
