#include <FastLED.h>

#define LED_PIN 5
#define NUM_LEDS 80
#define COLOR_ORDER GRB
#define LED_TYPE WS2811
#define FLASH_DELAY 500
#define BRIGHTNESS 10
CRGB leds[NUM_LEDS];

void setup() {
  // turn off all LEDs
  delay(3000);
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i].red = 255;
    leds[i].green = 55;
    leds[i].blue = 255;
  }
//  FastLED.setBrightness(0);
//  FastLED.show();
//
//  delay(2000);
  FastLED.setBrightness(0);
  FastLED.show();
}

void loop() {
  // put your main code here, to run repeatedly:
  FastLED.setBrightness(BRIGHTNESS);
  FastLED.show();
  delay(FLASH_DELAY);
  FastLED.setBrightness(0);
  FastLED.show();
  delay(FLASH_DELAY);

}
