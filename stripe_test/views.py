from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from django.conf import settings



class StripeView(TemplateView):
    template_name = 'stripe/payments.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    '''
    def get(self, request):

        key = settings.STRIPE_PUBLISHABLE_KEY

        return render(request,self.template_name,{'key':key})

        '''

