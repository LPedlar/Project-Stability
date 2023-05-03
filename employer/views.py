# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Course
# # Create your views here.

# def courses_view(request):
#     courses = Course.objects.order_by('course_title')
#     return render(request, 'courses/index.html', {'courses':courses})

# def course_detail(request, pk):
#     course = Course.objects.get(pk=pk)
#     return render(request, 'courses/course_detail.html', {'course':course})

