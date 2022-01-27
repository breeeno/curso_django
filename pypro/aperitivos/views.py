from django.shortcuts import render

class Video:
    def __init__(self, slug, titulo, youtube_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = youtube_id
videos = [
    Video( 'motivacao', 'Video Aperitivo: Motivação', 'F0cxaoZovy0' ),
    Video( 'instalacao-windows', 'Instalação Windows', 'IMCMip6kC40'),
]

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

