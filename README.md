# Grupo: Augusto Ortolan, Bruno Santos e Felipe Daniel

## Projeto G2 da disciplica de Computação Gráfica
**Proposta:**

A proposta é reconhecer e identificar funcionários de construções civis que entram no perímetro das construções sem o uso do capacete de proteção.
Além disso, foi aplicado neste projeto diversas técnicas de processamento de imagem. 

## Ferramentas Utilizadas
OpenCV.
DateTime.
Numpy.
Time.
CodeCs.
HaarCascade.
CascadeClassifier.
Reconhecimento de faces: haarcascade_frontalface_alt.

## Etapas de processamento:

1 - Estruturação do dataset de imagens para utilização no treinamento do objeto escolhido. (Capacete de segurança em construções)

2 - Preparação das imagens negativas.

3 - Criação das pastas: Positivas, Negativas e Treinamento.

4 - Aplicação dos seguintes códigos:

python buildListNegative.py

caminho bin opencv\opencv_annotation --annotations=saida.txt --images=positivas/

caminho bin opencv\opencv_createsamples -info saida.txt -bg negativas.txt -vec vetor.vec -w 24 -h 24

caminho bin opencv\opencv_traincascade -data treinamento -vec vetor.vec -bg negativas.txt -numPos 200 -numNeg 450 -w 24 -h 24 -

5 - Realização de testes após a conclusão do treinamento.

## Técnicas Utilizadas

1 - Mudanças de Cores;
2 - Binarização;
3 - Correção Morfológica;
4 - Seleção de Objetos por Cores;
5 - Recorte;
6 - Reconhecimento Facial;
7 - Detecção de Bordas;
8 - Redimensionamento;


## Saídas

Reconhecimento Facial
![reconhecimento](https://user-images.githubusercontent.com/57159392/142941433-1ccf635b-49df-4123-ac06-3ea5171173e4.png)

Redimensionamento de Imagem
![redimensionamento](https://user-images.githubusercontent.com/57159392/142941435-adc06b17-c6a5-49cd-a1c0-461cdc1fc093.png)

Trocar de cor
![trocarcor](https://user-images.githubusercontent.com/57159392/142941437-8a4de42b-aaaf-4404-99b1-9fbba61e7fea.png)

Binarização
![binarizacao](https://user-images.githubusercontent.com/57159392/142941443-791158d6-0f2c-4988-bf65-adf8bb50633f.png)

Bordas
![bordas](https://user-images.githubusercontent.com/57159392/142941445-2827315b-fe74-4d87-8fdc-7a572632f347.png)
