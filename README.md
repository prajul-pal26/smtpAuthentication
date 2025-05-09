docker-compose build
docker-compose up
pip freeze > requirements.txt
python manage.py runserver
pip install psycopg2-binary


# views
return render(request, 'app/index.html', context={'peoples':peoples})
we must remember the cotext word to render the dyanamic data to the frontend

# for loop in templates 
{%for i in list%}

{%endfor%}

# how to add css 
by add class in table , div or any think 
<table class = 'container>

# models
id = model.Autofield(   )                    generate the id PK

# using shell
python manage.py shell

from .api import utils.py
getNum(name='pranjul')    we can can any fucntion because that function is in django framework and e cant run direct 

# CRUD Operations
there are two methods to add the data in database

[1] - CREATE
1 - car=Case(diary_number='12', case_number='34')
2- Case.objects.create(diary_number='12', case_number='34')

[2] - READ
Case.objects.all()
Case.objects.get(id='1')
Case.objects.filter(id='1')
 point - add return __str__ in mmodel which help us to get the perticular name of that column

[3] - UPDATE
1-  case = Case.objects.get(id='1')
    case.name = 'deep'
    case.age = 23
2-  Case.objects.get(id='1').update(name='pragghf')

[4] - delete
Case.objects.get(id='1').delete()
