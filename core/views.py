from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()     #Envio de E-mail
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()  # limpa o formulário
        else:
            messages.error(request, 'Erro ao enviar o E-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

            # Envio de dados com POST
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']
            #
            # print('Mensagem enviada')
            # print(f'Nome: {nome}')
            # print(f'E-mail: {email}')
            # print(f'Assunto: {assunto}')
            # print(f'Mensagem: {mensagem}')



def produto(request):
    return render(request, 'produto.html')