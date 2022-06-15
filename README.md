# Embarcar uma IA em STM32F4
## Descrição
Embarcar em uma STM32F4 uma IA capaz de identificar os algarismos da base mnist. A IA utilizada foi o 
modelo pre treinado encontrado no seguinte repositório https://github.com/EN10/KerasMNIST.

## Função
Adquirir conhecimento sobre IAs em sistemas embarcados principalmente a ferramenta X-CUBE-AI da st.
O modelo em recebe por USB uma os ‘bytes’ referentes a uma imagem do banco mnist. A imagem é 28x28
preto e branco. A IA processa a imagem na STM32F4 e retorna um vetor de confianças.

## Motivação
Aplicação da metodologia aprendida no projeto do humanoide da RoboIme para poder equilibra-se com base em dados de sensores e feedback da posição dos motores.


## Diagrama de Blocks do Projeto
![alt text](https://raw.githubusercontent.com/YuriWit/microcon/main/images/DiagramaDeBlocosDoHardwere.png)

##  Pinout e Periféricos

| USB | PA12 | OTG_FS_DP            |
|-----|------|----------------------|
| USB | PA11 | OTG_FS_DM            |
| USB | PA10 | OTG_FS_ID            |
| USB | PA9  | VBUS_FS              |
| USB | PC0  | OTG_FS_PowerSwitchOn |
| USB | PD5  | OTG_FS_OverCurrent   |

## Fluxograma do Firmware
![alt text](https://raw.githubusercontent.com/YuriWit/microcon/main/images/FirmwareFluxogram.png)

## Principais pontos do código
Os principais documentos editados foram:
- ./Stm32MnistAI/USB_DEVICE/App/usbd_cdc_if.c
    - CDC_Receive_FS
    - CDC_Transmit_FS
- ./Stm32MnistAI/X-CUBE-AI/App/app_x-cube-ai.c
    - acquire_and_process_data
    - post_process
    - MX_X_CUBE_AI_Process