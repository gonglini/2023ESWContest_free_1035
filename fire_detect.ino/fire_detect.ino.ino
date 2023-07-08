const int flamePin = 9; 
const int flameDetected = 5;
int cnt =0;
int relay = 2;

serial_data = Serial.read();

void setup() {
  Serial.begin(9600); 
  pinMode(flamePin, INPUT);
  pinMode(relay,OUTPUT);
  
}

void loop() {
  int flameValue = digitalRead(flamePin); 

  if (flameValue == LOW) { 
    delay(500);
    cnt += 1;
    if (cnt > 5){
      Serial.println("fire");
      cnt == 0;
      delay(1000); // 
    }
  if(serial_data =='fire detected'){
    digitalWrite(flameDetected,HIGH);
    
  }
    
  if (serial_data == 'start'){
    digitalWrite(relay,HIGH);
    delay(8000);
  }
    flameValue == HIGH;
    flameDetected == LOW;
  }
}
