from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '669457570?h=ce33ebc40a'}
    return render(request, 'aperitivos/video.html', context= {'video': video})