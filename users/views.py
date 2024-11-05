from django.shortcuts import render, redirect




def home(request):
    return render(request, 'home.html')

# def signup(response):
     
#      if response.method ==  "POST":
#           form = SignUpForm(response.POST)
#           if form.is_valid():
#                form.save()
#           return redirect('home')
#      else:
#         form = SignUpForm()
#      return render(response, "signup.html" ,{"form":form})

def dashboard(request):
    return render(request, 'dashboard.html')

def logout(response):
     
     if response.method ==  "POST":
          return render (response, ' dashboard.html')
     else:
          return response(response, ' dashboard.html')
     
    