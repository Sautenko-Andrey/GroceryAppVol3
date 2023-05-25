from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import *
from captcha.fields import CaptchaField


class UploadItemNameForm(forms.ModelForm):
    '''Форма, которая будет принимать от пользователя
     назавание товара и сохранять его в БД
     для дальнейшей обработки.'''

    __USER_REQUEST_MAX_LENGTH = 50


    widgets = {
        'user_item_name': forms.TextInput(attrs={'class': 'form-input'}),
    }

    class Meta:
        model = UserItemNameUpload_2
        fields = ('user_item_name',)

    def clean_user_item_name(self):
        user_item_name = self.cleaned_data['user_item_name']
        if self.__USER_REQUEST_MAX_LENGTH < len(user_item_name):
            raise ValidationError('Слишком длинное название товара!')
        return user_item_name


class SearchByPhotoForm(forms.ModelForm):
    "Рабочая форма для загрузки пользовательских фото на сервер"

    class Meta:
        model = UserPhotoUploadModel_2
        fields = ['image', ]


class SearchDishesForm(forms.ModelForm):

    dish_name=forms.CharField(label='Название блюда',widget=forms.TextInput(attrs={'class':'form-input-dish'}))
    count_persons=forms.CharField(label='Количество людей',widget=forms.NumberInput(attrs={'class':'form-input-count'}))
    class Meta:
        model=Dishes
        fields=('dish_name','count_persons')


class AssembleProductSet(forms.ModelForm):
    product_name = forms.CharField(label='Название товара', widget=forms.TextInput(attrs={'class': 'form-input-dish'}))
    amount = forms.CharField(label='Количество',
                                    widget=forms.TextInput(attrs={'class': 'form-input-count-product-in-set'}))
    atb_choice = forms.BooleanField(label='АТБ',required=False)
    eko_choice = forms.BooleanField(label='ЭКО',required=False)
    varus_choice = forms.BooleanField(label='Varus',required=False)
    silpo_choice = forms.BooleanField(label='Сильпо',required=False)
    ashan_choice = forms.BooleanField(label='Ашан',required=False)
    novus_choice = forms.BooleanField(label='Novus',required=False)
    metro_choice = forms.BooleanField(label='Metro',required=False)
    nash_kray_choice = forms.BooleanField(label='Наш Край',required=False)
    fozzy_choice = forms.BooleanField(label='Fozzy',required=False)

    class Meta:
        model=SetOfProducts
        fields=('product_name','amount','atb_choice','eko_choice',
                'varus_choice','silpo_choice','ashan_choice',
                'novus_choice','metro_choice','nash_kray_choice',
                'fozzy_choice')


class UserRegisterForm(UserCreationForm):

    USERNAME_LENGTH_MIN=3
    USERNAME_LENGTH_MAX=20
    FORBIDDEN_DOMEN='.ru'


    username=forms.CharField(label='логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    email=forms.EmailField(label='email',widget=forms.TextInput(attrs={'class':'form-input'}))
    password1=forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='повторить пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha=CaptchaField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if self.USERNAME_LENGTH_MIN>len(username)>self.USERNAME_LENGTH_MAX:
            raise ValidationError('Слишком короткое или длинное имя пользователя!')
        return username

    def clean_email(self):
        email=self.cleaned_data['email']
        if email[-3:]==self.FORBIDDEN_DOMEN:
            raise ValidationError('Недопустимый email!')
        return email



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    #captcha = CaptchaField()