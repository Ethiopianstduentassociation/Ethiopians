# Welcome to Ethiopian Student Association

A Django charity website concept helping students affected by conflict and unsafe living conditions request relocation support, while enabling donors to learn about needs, contribute through Ethiopian banks, and share support stories.

## Features
- Student relocation support application saved to the database
- Private-by-default student applications and admin review
- Public support stories/blog with moderation through Django admin
- Donation instructions for Ethiopian bank transfers
- Responsive, classic gold, cream and forest-green visual theme
- Django admin for managing applications, stories and donation records

## Quick start
Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations association
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and the admin at http://127.0.0.1:8000/admin/.

## Important setup before public launch
1. In `esa_project/settings.py`, replace `SECRET_KEY` with a secure environment-based secret and set `DEBUG = False` in production.
2. Set `ALLOWED_HOSTS` to your domain.
3. Update bank names, account names and account numbers in `templates/association/donate.html` only after the organization verifies the accounts. The displayed bank details are placeholders and are not real payment destinations.
4. Configure HTTPS, secure backups, email delivery, spam protection, and a privacy policy.
5. Applications contain sensitive safety and contact information. Limit staff access, use strong admin passwords, and do not publish identifiable student information without explicit informed consent.
6. The contact options on public stories are intentionally mediated through the organization. Do not publish student phone numbers or exact locations.
7. This starter records applications but does not automatically arrange relocation, verify donations, or process bank payments online.

## Project layout
- `esa_project/`: Django settings and URLs
- `association/`: models, views, forms, admin
- `templates/association/`: page templates
- `static/association/`: styles and JavaScript
