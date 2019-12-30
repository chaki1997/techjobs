from django.apps import AppConfig


class PaypalSubscriptionConfig(AppConfig):
    name = 'paypal_subscription'
    #verbose_name = 'Paypal_subscription'

    def ready(self):
        # import signal handlers
        import paypal_subscription.signals
