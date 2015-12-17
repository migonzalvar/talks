

```
mkdir python-vigo
cd python-vigo
python3.4 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --upgrade wheel setuptools
pip install django
django-admin.py createproject pythonvigo
django-admin.py startproject pythonvigo
tree -d
cd pythonvigo
./manage.py migrate
./manage.py runserver
cd ..
deactivate
```
:
