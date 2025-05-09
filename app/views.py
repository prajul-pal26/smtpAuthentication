from django.shortcuts import render, redirect
from app.code.email_domain_verify import is_valid_email_domain
from app.code.email_sender import send_email
from django.contrib import messages

def main_page(request):
    # return render(request, 'app/main.html')
    return render(request, 'profile.html') 


def back(request):
    # return render(request, 'app/main.html')
    return render(request, 'back.html') 
     

def login(request):
    if request.method == "POST":
        if 'login' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            # Validate email domain
            if not is_valid_email_domain(email):
                messages.info(request, 'Email Domain Is Not Valid')
                return redirect('/login')
            
            # Send OTP
            otp = send_email(email)
            # Store user data and OTP in cookies (this is just one alternative to sessions)
            response = render(request, 'app/verify.html')
            response.set_cookie('genotp', otp)
            response.set_cookie('name', name)
            response.set_cookie('email', email)
            return response

        if 'verify' in request.POST:
            otp = request.POST.get('otp')
            # Retrieve OTP and other data from cookies
            genotp = request.COOKIES.get('genotp')
            if genotp != otp:
                messages.info(request, 'Invalid OTP')
                return redirect('/login')
            else:
                context = {"name": request.COOKIES.get('name')}
                
                # Clear cookies after successful login
                response = render(request, 'app/main.html', context)
                response.delete_cookie('genotp')
                response.delete_cookie('name')
                response.delete_cookie('email')
                
                return response

    return render(request, 'app/login.html')
