import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from model_bakery import baker
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client_com_usuario_logado, aula):
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
        assert_contains(resp, aula.titulo)


def test_youtube(resp, aula: Aula):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{ aula.youtube_id }')


def test_modulo_breadcrumb(resp, modulo:Modulo):
        assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


@pytest.fixture
def resp_sem_usuario(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_usuario_nao_logado_redirect(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))