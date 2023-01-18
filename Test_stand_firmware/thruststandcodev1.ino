#include "HX711.h" //load cell library
#include <Adafruit_ADS1X15.h> //ADC library
#include <Wire.h> //i2c library for interfacing with ADC
#include <Servo.h>

#define calibration_factor -99050 //Calibrtion factor for load cell

//pins for load cell amplifier
#define DOUT  3
#define CLK  2

HX711 scale;
Adafruit_ADS1115 ads;
Servo ESC;

void setup() {
  Serial.begin(115200);

  ESC.attach(5, 1000,2000);
 
  //initialization for loadcell amplifier
  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0

  //initialization for ADC
  /*
  ads.setGain(GAIN_SIXTEEN);    // 16x gain +/- 0.256V 1 bit = 0.125mV 0.0078125mV
  ads.begin();
*/
  
  Serial.println("Readings:");

}

void loop() {
  //int16_t results;
  //results = ads.readADC_Differential_0_1();
  //float amps = ((float)results * 256.0) / 32768.0;
  //Serial.print(3.6666*amps);
  //Serial.print("__");
  int airspeed = analogRead(A2);
  Serial.print(airspeed);
  Serial.print("   ");
  Serial.print(scale.get_units(), 1); //scale.get_units() returns a float

  
  Serial.println();
  
  

}
