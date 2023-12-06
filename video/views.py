from django.shortcuts import render,redirect
from django.http import HttpResponse
from celery.result import AsyncResult
from django.http import JsonResponse

import os
from django.conf import settings

import subprocess
import boto3

from .models import Video
from .tasks import process_video
# Create your views here.


s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_DEFAULT_REGION
)

dynamodb_client = boto3.client(
    'dynamodb',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_DEFAULT_REGION
)


def upload_video(request):
                  if request.method == 'POST':
                          video_file = request.FILES.get('videoFile')
                          if video_file:
                                  file_path = os.path.join(settings.MEDIA_ROOT, video_file.name)
                                  with open(file_path, 'wb') as f:
                                          for chunk in video_file.chunks():
                                                  f.write(chunk)

                                                  # Create a Video object in the database
                                                  video = Video.objects.create(video_file=video_file)

                                                  # Trigger the Celery task to process the video asynchronously
                                                  process_video.delay(video.id)


                                                # Cleanup: remove local files
                                                  os.remove(file_path)
                                                  os.remove(video.subtitle_file)          
                                                  
                                        

                                 

                                  return render (request, 'success.html')  
                          

                  return render(request, 'upload.html') 


def search_videos(request):
        if request.method == 'GET':
                keywords = request.GET.get('keyword')

                 # Retrieve time segments based on search keywords from Video model
                search_results = Video.objects.filter(Q(subtitles__icontains=keywords))

                context = {
                        'instance' : 'search_results'
                }

                return render(request,'search_results.html', 'context')
        return render(request,'search.html')


# to check the task status
def task_status(request):
    task_id = request.GET.get('task_id')
    task_result = AsyncResult(task_id)

    return JsonResponse({'status': task_result.status})
 
# create a view to retrieve and display the processed video URLs from Amazon S3
def success(request):
    return render(request, 'success.html')
                  

