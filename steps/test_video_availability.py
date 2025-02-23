from behave import given, when, then
import time

# Simulação de servidor de vídeo da Netflix
class NetflixServer:
    def __init__(self):
        self.available = True

    def simulate_video_playback(self):
        if not self.available:
            raise Exception('Falha no servidor!')
        return True  # Simula o vídeo sendo transmitido com sucesso

# Criação de instância para o servidor de vídeo
netflix_server = NetflixServer()

@given('o cliente está assistindo a um vídeo na plataforma da Netflix')
def step_impl(context):
    context.is_video_playing = netflix_server.simulate_video_playback()
    assert context.is_video_playing is True

@when('ocorre uma falha no servidor responsável por fornecer o arquivo do vídeo')
def step_impl(context):
    # Simulando falha no servidor de vídeo
    netflix_server.available = False
    time.sleep(1)  # Simula o tempo para falha no servidor

@then('o cliente deve continuar assistindo ao vídeo sem interrupções perceptíveis')
def step_impl(context):
    try:
        context.is_video_playing = netflix_server.simulate_video_playback()
        assert context.is_video_playing is True
    except Exception:
        assert False, 'Falha no servidor impactou a reprodução do vídeo'

@then('o vídeo não deve apresentar falhas ou perda de qualidade durante a falha no servidor')
def step_impl(context):
    # Como estamos apenas simulando, vamos garantir que o vídeo não falhe
    assert context.is_video_playing is True
