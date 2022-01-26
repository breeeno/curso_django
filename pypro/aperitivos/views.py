from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '669457570?h=ce33ebc40a'},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': '669916676?h=f9a20b60f7'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
