from rest_framework.views import exception_handler

def custom_exception_handler(exc,context):
    response=exception_handler(exc,context)
    exception_class=exc.__class__.__name__
    return response