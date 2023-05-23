from django.shortcuts import render
from django.http import HttpResponse

import shutil 

from .forms import getURL
import os

from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        # Path to the code on github
        path = './spotify_playlist_downloader/main.py'

        # Makes the temp folder "queue"
        queue_folder_path = os.path.join('.', 'queue')
        os.mkdir(queue_folder_path)
        TEMP_DIREC = './queue'
        
        # Receives the POST request and checks (Forms)
        form = getURL(request.POST)
        if form.is_valid():
            
            # Get the music
            url = form.cleaned_data['url']

            # Uses the playlist downlaoder in the console
            command = ['py', path, "-d " + TEMP_DIREC, url]
            os.system(' '.join(command))

            
            # Duplicating and Zipping queue into itself

            file_response = HttpResponse(content_type = 'application/zip')
            shutil.make_archive('./queue', 'zip', '.', 'queue')

            with open('./queue.zip', 'rb') as f:
                file_response.write(f.read())


            os.remove('./queue.zip')
            shutil.rmtree('./queue')
            return file_response
        
        else:
            return HttpResponse("Invalid form data.")

    else:
        form = getURL()
    return render(request, "playlist_downloader/URLform.html", {"form": form})