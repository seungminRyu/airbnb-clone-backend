from django.http import HttpResponse
from datetime import datetime


def say_hello(request):
    return HttpResponse("hello!")


def say_hello_with_time(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"현재시간: {current_time}")


def request_info(request):
    request_info = {
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
        "body": request.body,
    }
    return HttpResponse(f"요청 정보: {request_info}")
