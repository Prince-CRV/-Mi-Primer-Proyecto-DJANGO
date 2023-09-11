from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions']) # al usar model_to_dict hay que tener cuidado porque hay cosas en el mo9delo que no se pueden convertir bien, por tanto hay que excluirlas ver clase 77
        item['last_login'] = self.last_login.strftime('%Y-%m-%d') # convierto este parametro para poderlo usar, ver clase 77
        item['date_joined'] = self.last_login.strftime('%Y-%m-%d') # convierto este parametro para poderlo usar, ver clase 77
        item['image'] = self.get_image() # convierto este parametro para poderlo usar, ver clase 77
        return item
