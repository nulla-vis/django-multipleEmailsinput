from django.shortcuts import redirect, render
from .models import User, Email
from .forms import EmailForm, EmailListsForm, EmailsForm


def test_email(request):
    user = User.objects.get(pk=1)

    if request.method == 'POST':

        # can use form.HiddenInput to get value
        emailListForm = EmailListsForm(request.POST)

        if emailListForm.is_valid():
            emailList = emailListForm.cleaned_data['emailList']
            # remove unnecessary character(s)
            emailList = emailList.replace(
                '"', '').replace('[', '').replace(']', '')
            # convert string to list
            emails = list(emailList.split(','))

            for email in emails:
                # validate email
                emailForm = EmailsForm({'email': email})
                if emailForm.is_valid():
                    Email.objects.create(user=user, email_list=email)
                else:
                    print('nope')

        return redirect('test_email')

    contex_data = {}

    return render(request, 'test/test_email.html', contex_data)
