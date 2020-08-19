int redPin = 9;
int greenPin = 10;
int bluePin = 11;
String code = "";
int color = 0;

void setup() {
    Serial.begin(9600);
    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}

void loop() {
    int colors[4][3] =
    {
    {0, 255, 0},
    {255, 70, 0},
    {255, 25, 0},
    {255, 0, 0}
    };

    if (Serial.available() > 0) {
        code = Serial.readString();
        color = code.toInt();
    }
    
    setColor(colors[color][0], colors[color][1], colors[color][2]);
    
}

void setColor(int redValue, int greenValue, int blueValue) {
    analogWrite(redPin, redValue);
    analogWrite(greenPin, greenValue);
    analogWrite(bluePin, blueValue);
}
