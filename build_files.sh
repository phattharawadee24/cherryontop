
pip install --upgrade pip
pip install -r requirements.txt

python3 some_script.py
python manage.py collectstatic --noinput

# Make migrations
python manage.py makemigrations
python manage.py migrate