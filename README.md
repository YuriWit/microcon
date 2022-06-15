# Embarcar IA em STM
## Descricao
Embarcar em uma STM32 uma IA capaz de identificar os algarismos da base mnist. A IA utilizada foi o 
medelo pre treinado encontrado no seguinte repositorio https://github.com/EN10/KerasMNIST.

## Funcao
Adquirir conhecimento sobre IAs em sistemas embarcados principalmente a ferramenta X-CUBE-AI da stm32.

## Motivacao
Aplicacao da metodologia no projeto do humanoid da RoboIme equilibra-se com base em dados de sensores e
feedback dos motores.


## Diagrama de Blocks do Projeto
![alt text](https://raw.githubusercontent.com/YuriWit/microcon/main/images/DiagramaDeBlocosDoHardwere.png)

##  Pinout

| USB | PA12 | OTG_FS_DP            |
|-----|------|----------------------|
| USB | PA11 | OTG_FS_DM            |
| USB | PA10 | OTG_FS_ID            |
| USB | PA9  | VBUS_FS              |
| USB | PC0  | OTG_FS_PowerSwitchOn |
| USB | PD5  | OTG_FS_OverCurrent   |

## Fluxograma do Firmware
![alt text](https://raw.githubusercontent.com/YuriWit/microcon/main/images/FirmwareFluxogram.png)
