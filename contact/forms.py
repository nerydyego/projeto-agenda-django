from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'classe-a classe-b',
                'placeholder' : 'Aqui veio da variavel first_name',
            }
        ),
        label= 'Primeiro Nome',
        help_text = 'Texto de ajuda para o usúario',
    )
    # Maneiras de manipular widget
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class-a class-b',
    #         'placeholder': 'aqui veio do init super',
    #     })
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',
                )
        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             'class':'classe-a',
        #             'placeholder' : 'Escreva Aqui!',
        #         }
        #     )
        # }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        # self.add_error(
        #     'first_name', 
        #     ValidationError(
        #         "Mensagem de erro!", 
        #         code='invalid'
        #     )
        # )
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome igual primeiro nome, não e permitido',
                    code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
            
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        # print('Passei no clean do first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                'Não digite ABC neste campo',
                code='invalid'
                )
            )
        return first_name