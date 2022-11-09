#include <Arduino.h>
TaskHandle_t Tarea1;
int cuenta = 0;
void loop2(void *parametro){
  while (true)
  {
    Serial.println("\t\t\tEl nucleo--> "+ String(xPortGetCoreID()));
    delay(100);

  }
  vTaskDelay(10);
}

void setup(){
  xTaskCreatePinnedToCore(
    loop2,
    "Tarea1",
    1000,
    NULL,
    1,
    &Tarea1,
    0
  );
  Serial.begin(115200);
}

void loop(){
  Serial.println("El nucleo--> "+ String(xPortGetCoreID()));
  delay(1000);
}
