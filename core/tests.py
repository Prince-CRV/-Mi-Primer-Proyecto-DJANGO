
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_1.settings')
django.setup()

from core.models import Type
from core.models import Employee

# Type.objects.create(name='preuba')
#Type.objects.create(name='pr2')

# Create your tests here.
#query = Type.objects.all()
#print(query)

#insertar
#t = Type()
#t.name = 'Accionistakllklklk'
#t.save()

#editar
#t = Type.objects.get(id=3)
#t.name = 'prrruebbbaaaaa'
#t.save()

#eliminar
#t = Type.objects.get(id=3)
#t.delete()

#obj = Type.objects.filter(name__icontains='terry') #contains=> es las letras exactas, icontains busca mayuscula o minuscula
#obj = Type.objects.filter(name__startswith='p')
#obj = Type.objects.filter(name__endswith='a')
#obj = Type.objects.filter(name__endswith='a').count()
#obj = Type.objects.filter(name__endswith='a').exclude(id=5)
#obj = Employee.objects.filter(type_id=1)
#print(obj)
for i in Type.objects.filter(name__endswith='a'):
    print(i.name)
