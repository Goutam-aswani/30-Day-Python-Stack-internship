echo " BUILD START"
python 3.13 -m pip install -r requirements.txt
python 3.13 manage.py collectstatic --noinput --clear
echo " BUILD END"

