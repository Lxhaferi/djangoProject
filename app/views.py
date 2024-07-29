from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    if request.method == 'POST':
        Name = request.POST.get('Name')
        Subject = request.POST.get('Subject')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')

        data = {
            'Name': Name,
            'Subject': Subject,
            'Email': Email,
            'Message': Message,
        }
        Message = '''
        New message: 
        {}
        
        From: 
        {}
        '''.format(data['Message'], data['Email'])
        send_mail(data['Subject'], Message, '', ['loreweblore@gmail.com'])

    return render(request, 'index.html', context)