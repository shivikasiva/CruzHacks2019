
// Include the libraries that we'll be using throughout the code
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

Servo blindServo;
//Duration required to open blinds (ms)
int openDelay = 20000; 
//Duration required to close blinds (ms)
int closeDelay = 20000; 

// Define the ID and password of your Wi-Fi network
const char* ssid = "Bees";
const char* password = "12345678";

// Instantiate the ESP8266WebServer class, passing the argument 80 for the
// port that the server will be listening.
ESP8266WebServer server(80);





// User-defined function that will be called when a client accesses the root
// directory path of the ESP8266 host


void handleRoot() {
  // Simply sends an 'OK' (200) response to the client, and a plain text
  // string with usage.
  server.send(200, "text/plain", String("Hello from esp8266! Usage: navigate to") +
              String(" /setblinds?blinds=XX changing XX to UP or DOWN."));
}

// User-defined function that will be called when a client accesses the /setblinds
// path of the ESP8266 host
void handleSetBlinds() {


  String blinds_status = server.arg("blinds");

  
  // Check if the URL include a change of the blinds status
  bool url_check = false;
  if((blinds_status == "UP")||(blinds_status == "DOWN")||(blinds_status =="STOP"))
    url_check = true;


  if (blinds_status == "UP") {
    //Sets continuous rotation servo to max velocity in + direction
     blindServo.attach(5);
    Serial.write("Blinds going up!");
    blindServo.write(160); 
    
  }
  else if (blinds_status == "DOWN") {
    //Sets continuous rotation servo to max velocity in + direction
     blindServo.attach(5);
    Serial.write("Blinds going down!");
    blindServo.write(0); 
    
  }

  else if (blinds_status == "STOP") {
    //Sets continuous rotation servo to max velocity in + direction
     blindServo.attach(5);
    Serial.write("Blinds STOPPING!");
    
    
    blindServo.write(80);
     blindServo.detach();
  }

  if (url_check)
    // If we've set the blinds to the requested status, we have the webserver
    // return an "OK" (200) response.  We also include the number of milliseconds
    // since the program started running.
    // Note: This number will overflow (go back to zero), after approximately 50 days.
    server.send(200, "text/plain", "Blinds State Changed! (" + String(millis()) + ")");
  else
    server.send(200, "text/plain", "Blinds State Unchanged! (" + String(millis()) + ")");
}

// If the client requests any other URL than the root directory or the /setblinds path:
void handleNotFound() {
  // We construct a message to be returned to the client
  String message = "File Not Found\n\n";
  // which includes what URI was requested
  message += "URI: ";
  message += server.uri();
  // what method was used
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  // and what parameters were passed
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  // the response, as expected, is a "Not Found" (404) error
  server.send(404, "text/plain", message);
}

// In the setup function we initialize the different things
// that will be needed in our program, as well as set up the hardware
void setup(void) {


 


  // Start the Serial communication for debugging purposes
  Serial.begin(115200);
  //  Initialize the WiFi client and try to connect to our Wi-Fi network
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for a successful connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // For debugging purposes print the network ID and the assigned IP address
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Associate the URLs with the functions that will be handling the requests
  server.on("/", HTTP_GET, handleRoot);
  server.on("/setblinds", HTTP_GET, handleSetBlinds);
  server.onNotFound(handleNotFound);

  // Start running the webserver
  server.begin();
  Serial.println("HTTP server started");
}

// The loop function is straight-forward, simply handle any incoming requests to the
// our ESP8266 host!
void loop(void) {
  server.handleClient();
}
