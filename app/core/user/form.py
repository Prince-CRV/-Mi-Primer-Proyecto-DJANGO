from django.forms import *
from django import forms

from core.user.models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image', 'groups'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': forms.PasswordInput(
                render_value=True,
                attrs={
                    'placeholder': 'Ingrese una contraseña',
                }
            ),
            'groups': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple',
            })
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                # la siguiente lógica se usará para que al crear un usuario se encripote en md5 la password
                pwd = self.cleaned_data['password'] # obtengo el password
                u = form.save(commit=False) # pausa
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
                u.groups.clear()

                # la siguiente lógica es para guardar los grupos

                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': forms.PasswordInput(
                render_value=True,
                attrs={
                    'placeholder': 'Ingrese una contraseña',
                }
            ),
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active', 'groups']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                # la siguiente lógica se usará para que al crear un usuario se encripote en md5 la password
                pwd = self.cleaned_data['password'] # obtengo el password
                u = form.save(commit=False) # pausa
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
