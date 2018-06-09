from django.shortcuts import render
from django.template.response import TemplateResponse
from instruments.models import Instruments
from django.views.generic import TemplateView
from instruments.forms import HireForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def instruments(request):
    data = Instruments.objects.all()
    return TemplateResponse(request,'pages/instruments.html', {"data" : data}) # curly braces dictionary list


class Instrument(TemplateView):
    template_name = "pages/instrument_form.html"

    def get(self, request):
        form = HireForm()
        return render(request, self.template_name, {'form' : form})
    
    def post(self,request):
        form = HireForm(request.POST)
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        instrument = request.POST.get('instrument')
        days = request.POST.get('days')
 
        
        subject = 'New Instrument Hire Request'
        message = (
            'Hire Request from' + '\n' + id + '\n' + first_name +
            '\n' + last_name + '\n' + instrument + '\n' + days)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'testdevelopmentuser1@gmail.com' ] 
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return TemplateResponse(request, self.template_name, {'form' : form})

'''
####
# 
# whatever is passed above runs server side (not static)
#
#
##
    #data = Instruments.objects.filter(name="jazz flute") # still returns a set
    #data = Instruments.objects.get(name="jazz flute") # return single object
    #data = Instruments.objects.get(pk=1) # return by primary key

'''