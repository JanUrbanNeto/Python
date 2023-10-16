// Definir os pinos dos motores
#define MOTOR_DIREITO_FRENTE 3
#define MOTOR1B 4
#define MOTOR2A 5
#define MOTOR2B 6

// Definir os pinos dos sensores
#define SENSOR1 A0
#define SENSOR2 A1
#define SENSOR3 A2

// Definir os limiares de luminosidade
#define LIMIAR1 500
#define LIMIAR2 700

// Definir as funções de movimentação dos motores
void PararMotor1() {
  digitalWrite(MOTOR_DIREITO_FRENTE, LOW);
  digitalWrite(MOTOR1B, LOW);
}

void FrenteMotor1() {
  digitalWrite(MOTOR_DIREITO_FRENTE, HIGH);
  digitalWrite(MOTOR1B, LOW);
}

void ReversoMotor1() {
  digitalWrite(MOTOR_DIREITO_FRENTE, LOW);
  digitalWrite(MOTOR1B, HIGH);
}

void PararMotor2() {
  digitalWrite(MOTOR2A, LOW);
  digitalWrite(MOTOR2B, LOW);
}

void FrenteMotor2() {
  digitalWrite(MOTOR2A, HIGH);
  digitalWrite(MOTOR2B, LOW);
}

void ReversoMotor2() {
  digitalWrite(MOTOR2A, LOW);
  digitalWrite(MOTOR2B, HIGH);
}

// Inicializar as variáveis globais
int valor1, valor2, valor3; // Valores dos sensores

void setup() {
  // Configurar os pinos dos motores como saída
  pinMode(MOTOR_DIREITO_FRENTE, OUTPUT);
  pinMode(MOTOR1B, OUTPUT);
  pinMode(MOTOR2A, OUTPUT);
  pinMode(MOTOR2B, OUTPUT);

  // Configurar os pinos dos sensores como entrada
  pinMode(SENSOR1, INPUT);
  pinMode(SENSOR2, INPUT);
  pinMode(SENSOR3, INPUT);

  // Parar os motores inicialmente
  PararMotor1();
  PararMotor2();
}

void loop() {
  // Ler os valores dos sensores
  valor1 = analogRead(SENSOR1);
  valor2 = analogRead(SENSOR2);
  valor3 = analogRead(SENSOR3);

  // Se nenhum sensor detectar luz suficiente, parar os motores
  if (valor1 < LIMIAR1 && valor2 < LIMIAR1 && valor3 < LIMIAR1) {
    PararMotor1();
    PararMotor2();
  }

  // Se o sensor da esquerda detectar mais luz que o da direita, girar para a esquerda
  else if (valor1 > LIMIAR2 && valor3 < LIMIAR2) {
    ReversoMotor1();
    FrenteMotor2();
  }

  // Se o sensor da direita detectar mais luz que o da esquerda, girar para a direita
  else if (valor3 > LIMIAR2 && valor1 < LIMIAR2) {
    FrenteMotor1();
    ReversoMotor2();
  }

  // Se o sensor do meio detectar mais luz que os outros, ir em frente
  else if (valor2 > LIMIAR2 && valor1 < LIMIAR2 && valor3 < LIMIAR2) {
    FrenteMotor1();
    FrenteMotor2();
  }

}