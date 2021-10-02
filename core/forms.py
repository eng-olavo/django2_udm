from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='None', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', max_length=100)