int v = 0;
int controle = 0;

void setup() {
  pinMode(10, INPUT_PULLUP);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  
  digitalWrite(5, HIGH);
}

void loop() {
  v = digitalRead(10);
  if(v == HIGH) {
    digitalWrite(5, LOW);
  	digitalWrite(3, HIGH);
    controle = 1;
  } else {
    while(controle != 0){
      digitalWrite(3, LOW);
      digitalWrite(6, HIGH);
      delay(3000);
      digitalWrite(6, LOW);
      digitalWrite(5, HIGH);
      controle = 0;
      break;
    }
  }
}