from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # **signup page save krne pe jo data hum ne file kiya vo na delete ho or jo error hai vo file kre hum**
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_massage = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,

                            email=email,
                            password=password)

        error_massage = self.validateCustomer(customer)

        if not error_massage:
            print(first_name, last_name, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_massage,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_massage = None
        if (not customer.first_name):
            error_massage = "Enter your first name !!"

        elif len(customer.first_name) < 4:
            error_massage = "First Name must be 4 character long or more"

        elif not customer.last_name:
            error_massage = "Last Name Required"

        elif len(customer.last_name) < 4:
            error_massage = "Last Name must be 4 character long or more"

        elif len(customer.password) < 6:
            error_massage = 'Password must be 6 character long'

        elif len(customer.email) < 5:
            error_massage = "Email Must be 5 character long"
            # ****ye btayega agar customer ka email pehle se registered hai toh error dega*****
        elif customer.isExists():
            error_massage = 'Email Address Already Registered'

        return error_massage
