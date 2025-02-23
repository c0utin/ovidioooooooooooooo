# Testes de Disponibilidade da Netflix

## Visão Geral
Este projeto demonstra como a Netflix garante a **disponibilidade** de seus serviços de streaming, mesmo em caso de falha nos servidores de origem dos vídeos. Para isso, utilizamos **testes comportamentais (BDD)** com **Gherkin e Behave**, cobrindo tanto requisitos funcionais (RF) quanto não funcionais (RNF), conforme exigido na atividade.

## Requisitos Atendidos

### 1. Documentação dos Requisitos em Código (1 RF - 5.0 pontos)
Para garantir que o vídeo continue a ser transmitido mesmo com falhas no servidor, documentamos esse requisito em código usando Gherkin no arquivo `video_availability.feature`. O cenário descreve a necessidade de garantir a continuidade do serviço para o usuário final, atendendo à característica de **disponibilidade** da **ISO 25010**.

### 2. Aferição da Qualidade dos Requisitos no Sistema (1 RNF - 5.0 pontos)
A qualidade desse requisito foi testada implementando um **servidor de vídeo simulado** em Python, no qual verificamos se o sistema pode lidar com falhas do servidor sem impactar a experiência do usuário. O foco está na **resiliência**, garantindo que o sistema reaja de forma robusta a falhas.

## Relação com a ISO 25010
A **ISO/IEC 25010** define as características de qualidade de software. Neste projeto, abordamos principalmente:
- **Disponibilidade:** O vídeo deve continuar sendo reproduzido mesmo quando um servidor falha.
- **Resiliência:** O sistema deve se recuperar automaticamente, redirecionando a requisição para outro servidor sem impactar a experiência do usuário.

## Estrutura do Projeto
```
/netflix_test/
│
├── /features/                      # Arquivos Gherkin
│   ├── video_availability.feature  # Requisitos funcionais em Gherkin
│
├── /steps/                         # Implementação dos steps em Python
│   ├── test_video_availability.py  # Código de teste
│
├── requirements.txt                # Dependências do projeto
└── setup.sh                         # Script de configuração e execução
```

## Arquivos Principais

### 1. `video_availability.feature`
Arquivo Gherkin que define o requisito de **disponibilidade**:
```gherkin
Feature: Garantia de Disponibilidade do Vídeo

  Scenario: O vídeo continua a ser transmitido mesmo com falha no servidor
    Given o cliente está assistindo a um vídeo na plataforma da Netflix
    When ocorre uma falha no servidor responsável por fornecer o arquivo do vídeo
    Then o cliente deve continuar assistindo ao vídeo sem interrupções perceptíveis
    And o vídeo não deve apresentar falhas ou perda de qualidade durante a falha no servidor
```

### 2. `test_video_availability.py`
Implementação em Python que simula um servidor e testa se o vídeo continua rodando mesmo com falhas.
```python
from behave import given, when, then
import time

# Simulação de servidor de vídeo da Netflix
class NetflixServer:
    def __init__(self):
        self.available = True

    def simulate_video_playback(self):
        if not self.available:
            raise Exception("Falha no servidor!")
        return True

# Instância do servidor
netflix_server = NetflixServer()

@given('o cliente está assistindo a um vídeo na plataforma da Netflix')
def step_impl(context):
    context.is_video_playing = netflix_server.simulate_video_playback()
    assert context.is_video_playing is True

@when('ocorre uma falha no servidor responsável por fornecer o arquivo do vídeo')
def step_impl(context):
    netflix_server.available = False
    time.sleep(1)

@then('o cliente deve continuar assistindo ao vídeo sem interrupções perceptíveis')
def step_impl(context):
    try:
        context.is_video_playing = netflix_server.simulate_video_playback()
        assert context.is_video_playing is True
    except Exception:
        assert False, "Falha no servidor impactou a reprodução do vídeo"

@then('o vídeo não deve apresentar falhas ou perda de qualidade durante a falha no servidor')
def step_impl(context):
    assert context.is_video_playing is True

   ```

## Conclusão
Este projeto demonstra como a Netflix pode garantir a **disponibilidade** do serviço de streaming, mesmo em casos de falha. Utilizamos **Gherkin para documentar os requisitos funcionais e não funcionais**, além de **Python com Behave para validar a qualidade do requisito**. Isso reforça a aderência à **ISO 25010**, garantindo um software resiliente e confiável.


