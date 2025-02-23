Feature: Garantia de Disponibilidade do Vídeo

  Scenario: O vídeo continua a ser transmitido mesmo com falha no servidor
    Given o cliente está assistindo a um vídeo na plataforma da Netflix
    When ocorre uma falha no servidor responsável por fornecer o arquivo do vídeo
    Then o cliente deve continuar assistindo ao vídeo sem interrupções perceptíveis
    And o vídeo não deve apresentar falhas ou perda de qualidade durante a falha no servidor
