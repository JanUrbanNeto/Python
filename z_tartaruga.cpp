// Definir os pinos dos motores
#define MOTOR_DIREITO_FRENTE 3
#define MOTOR_DIREITO_REVERSO 4
#define MOTOR_ESQUERDO_FRENTE 5
#define MOTOR_ESQUERDO_REVERSO 6

// Definir os pinos dos sensores
#define SENSOR_LUMINOSIDADE_FRENTE A0
#define SENSOR_LUMINOSIDADE_DIREITO A1
#define SENSOR_LUMINOSIDADE_ESQUERDO A2

// Definir os limiares de luminosidade
#define LIMIAR1 500
#define LIMIAR2 700

// Inicializar as variáveis globais
int valor1, valor2, valor3; // Valores dos sensores

void setup() {
  // Configurar os pinos dos motores como saída
  pinMode(MOTOR_DIREITO_FRENTE, OUTPUT);
  pinMode(MOTOR_DIREITO_REVERSO, OUTPUT);
  pinMode(MOTOR_ESQUERDO_FRENTE, OUTPUT);
  pinMode(MOTOR_ESQUERDO_REVERSO, OUTPUT);

  // Configurar os pinos dos sensores como entrada
  pinMode(SENSOR_LUMINOSIDADE_FRENTE, INPUT);
  pinMode(SENSOR_LUMINOSIDADE_DIREITO, INPUT);
  pinMode(SENSO_LUMINOSIDADE_ESQUERDO3, INPUT);

  // Parar os motores inicialmente
  PararMotor1();
  PararMotor2();
}

void loop() {
  
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