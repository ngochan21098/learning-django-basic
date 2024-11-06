from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class CustomMiddlewareIP(MiddlewareMixin):
  def process_request(self, request):
    print("process_request")
    allowed_ips = ['192.168.1.1', '123.123.123.123', '127.0.0.2'] # Authorized ip's
    ip = request.META.get('REMOTE_ADDR') # Get client IP
    print("ip", ip)
    if ip not in allowed_ips:
      return HttpResponseForbidden("Ip not allowed!") # If user is not allowed raise Error

    # If IP is allowed we don't do anything
    return None
