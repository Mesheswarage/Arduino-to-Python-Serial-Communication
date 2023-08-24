#define inputPin A0
#define outputPin 4

void setup() {
  pinMode(inputPin, INPUT);
  Serial.begin(9600);
  pinMode(outputPin,OUTPUT);
}

int val;
void loop() {
  val = analogRead(inputPin);
  float V = (5.0 / 1024.0) * val;
  Serial.println(V);
  if (V > 4.8){
    Serial.println("yo");
    digitalWrite(outputPin, HIGH);
  }
  else{
    Serial.println("No");
    digitalWrite(outputPin, LOW);
  }
  delay(500);
}
