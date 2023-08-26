from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View

from HeartHeal.models.user import User


class Login(View):
    return_url = None

    def get(self, request):
        if ('user' not in request.session):
            Login.return_url = request.GET.get('return_url')
            return render(request, 'login.html')
        return redirect('dashboard')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_user_by_email(email)
        error_message = None
        if user:
            if user.role == 'doctor':
                if user.password == password:
                    request.session['user'] = user.id
                    request.session['role'] = user.role

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('dashboard')
            else :
                flag = check_password(password, user.password)
                if flag:
                    request.session['user'] = user.id
                    request.session['role'] = user.role

                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('dashboard')
                else:
                    error_message = 'Sai mật khẩu !!'
        else:
            error_message = "Tài khoản không tồn tại !!"

        return render (request, 'login.html', {
            'error': error_message
        })

