
#include <Arduino.h>
// Declaracion de variables
long value;
String inputString;
// Declaracion de funcion de recepcion y envios de datos

void SerialEvent(long);
// Configuracion
void setup(){
  Serial.begin(115200);
  randomSeed(analogRead(15));
  }
// Bucle infinito 
void loop(){
  delay(100);
  value = analogRead(15);
  SerialEvent(value);
  }
// Funcion de recepcion y envio de datos 
void SerialEvent(long value){
  while(Serial.available()){
    char inputChar = Serial.read();                   // lee puerto serial
    inputString += inputChar;                       
    }
    if(inputString.indexOf("getValue")>=0){
      String json_data = "{\"Value\":" + (String)value+ "}";
      Serial.println(json_data);  
    } 
    inputString = "";
  }