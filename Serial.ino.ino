int data[500];
int bob = 0;
  
void setup() {
Serial.begin(9600); // setup serial
}

void loop() {
  // set up the time range
  for(int n = 0; n <= 499; n++)
    data[n] = n;

  // passing the data through 
  for(int i = 0; i <= (sizeof(data)/sizeof(int))-1; i++)
  {
    if(data[i]%5 == 0){bob++;}  
    
    Serial.print(data[i]);
    Serial.print(',');
    Serial.println(bob);
    
    delay(250);
  } 
}
