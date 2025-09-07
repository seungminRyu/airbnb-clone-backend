from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms, "title": "안녕하세요! 방을 보여드립니다."}

    return render(
        request,
        "all_rooms.html",
        context,
    )


def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        return render(request, "room_detail.html", {"room": room})
    except Room.DoesNotExist:
        return render(
            "room_detail.html",
            "",
            {
                "not_found": True,
            },
        )


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
