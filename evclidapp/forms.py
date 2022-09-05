from django import forms


class AppealForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'footer__input input-name',
                'placeholder': 'Фамилия, Имя, Отчество'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'footer__input input-mail',
                'placeholder': 'E-mail'
            }
        )
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'footer__area message-area',
                'placeholder': 'Сообщение',
                'cols': 30,
                'rows': 6
            }
        )
    )

    check_box = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'footer__checkbox'
            }
        )
    )
