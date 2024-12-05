from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden


class AllowedIDMiddleware (MiddlewareMixin):
    #  def __init__(self, get_response):
    #      self.get_response = get_response
    #      self.allowed_ids = ['123', '456', '789']  
    #  def __call__(self, request):
    #     user_id = request.GET.get('user_id')  

    #     if user_id not in self.allowed_ids:
    #         return HttpResponse(status = 403)
    
    #     response = self.get_response(request)
    #     return response
     

    #  Check if client IP is allowed
    def process_request(self, request):
        allowed_ips = ['192.168.1.1', '123.123.123.123', '127.0.0.1'] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP
        if ip not in allowed_ips:
         return HttpResponseForbidden("Ip not allowed!") # If user is not allowed raise Error

    # If IP is allowed we don't do anything
        return None
     
class RequireCustomHeaderMiddleware (MiddlewareMixin):
    def process_request(self, request):
    # Check if the required header is present
        expected_api_key = '123456'
        path = request.META.get('PATH_INFO', '')
        print(path)
        if '/users' in path:
            if request.META.get('HTTP_API_KEY') != expected_api_key:
                return HttpResponseForbidden("Forbidden: Missing required header")
        
    # Proceed with the request if header is present
        return None
    
class RequireCustomResponseMiddleware (MiddlewareMixin):
    def process_response(self, request, response):
        # Retrieve your custom session_id or generate one
        # For example, you can use Django's session ID or any custom session ID logic here
        custom_session_id = "123"

        # Add the custom session_id to the response header
        response['session_id'] = custom_session_id
        
        return response