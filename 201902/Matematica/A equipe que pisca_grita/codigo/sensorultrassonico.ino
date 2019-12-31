#include <Ultrasonic.h> //Importação da biblioteca do módulo HC-SR04.

//Define os pinos para o trigger e echo.
#define pino_trigger 6 
#define pino_echo 7

//Lugar de cada LED e BUZZER nas portas do Arduino.
int distancia = 0;
int LED_Blue = 8;
int LED_Green = 9;
int LED_Yellow = 10;
int LED_Red = 11;
int Buzzer = 12;
 
Ultrasonic ultrasonic(pino_trigger, pino_echo); // Inicializa nos pinos Trigger e Echo definidos.

void setup() 
{
  Serial.begin(9600); //Monitor para verificar a distância.
  //Função que configura a saída dos pinos(pinMode).
  pinMode(LED_Blue, OUTPUT);
  pinMode(LED_Green, OUTPUT);
  pinMode(LED_Yellow, OUTPUT);
  pinMode(LED_Red, OUTPUT);
  pinMode(Buzzer, OUTPUT);
}
 
void loop() //Função de laço de repetição usada para Arduino
{
  //Le as informações do sensor, em centimetros
  int distancia;
  long microsec = ultrasonic.timing();
  distancia = ultrasonic.convert(microsec, Ultrasonic::CM);
  Serial.print("Distância em cm: ");
  Serial.println(distancia);

  // 0 é quando o LED/Buzzer está desligado, e 1 para quando o LED/Buzzer está ligado.
    if ( distancia > 200 )
  {
  //Função liga/desliga (digitalWrite) própria do arduino.
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  }
  else if (distancia > 150)
  {
  digitalWrite(LED_Blue, 1);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 1);
  delay (500); //500 microsegundos que permanece desligado.
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (500);
  }
  else if ( distancia > 120 )
  {
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 1);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 1);
  delay (350);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (350);
  }
  else if ( distancia > 80 )
  {
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 1);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 1);
  delay (285);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (285);
  }
  else if ( distancia > 50 )
  {
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 1);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 1);
  delay (240);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (240);
  }
  else if ( distancia > 30 )
  {
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 1);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 1);
  delay (200);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (200);
  }
  else if ( distancia > 15 )
  {
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 1);
  digitalWrite(Buzzer, 1);
  delay (150);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (150);
  }
  else if (distancia > 8 )
  {
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 1);
  digitalWrite(Buzzer, 1);
  delay (100);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (100);
  }
  else if ( distancia <= 8 )
  {
  digitalWrite(LED_Blue, 1);
  digitalWrite(LED_Green, 1);
  digitalWrite(LED_Yellow, 1);
  digitalWrite(LED_Red, 1);
  digitalWrite(Buzzer, 1);
  delay (50);
  digitalWrite(LED_Blue, 0);
  digitalWrite(LED_Green, 0);
  digitalWrite(LED_Yellow, 0);
  digitalWrite(LED_Red, 0);
  digitalWrite(Buzzer, 0);
  delay (50);
  }
}
