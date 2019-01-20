// Include the libraries that we'll be using throughout the code
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

Servo lightServo;
//Duration required to open lights (ms)

//Duration required to close lights (ms)


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
              String(" /setlights?lights=XX changing XX to UP or DOWN."));
}

// User-defined function that will be called when a client accesses the /setlights
// path of the ESP8266 host
void handleSetlights() {


  String lights_status = server.arg("lights");

  
  // Check if the URL include a change of the lights status
  bool url_check = false;
  if((lights_status == "UP")||(lights_status == "DOWN"))
    url_check = true;


  if (lights_status == "ON") {
    //Sets continuous rotation servo to max velocity in + direction
    Serial.write("lights going on!");
    lightServo.attach(5);
    lightServo.write(75); 
    delay(300);
    lightServo.detach();

     
  }
  else if (lights_status == "OFF") {
    //Sets continuous rotation servo to max velocity in + direction
    Serial.write("lights going off!");
    lightServo.attach(5);
    lightServo.write(0); 
    delay(300);
    lightServo.detach();
    
  }

  if (url_check)
    // If we've set the lights to the requested status, we have the webserver
    // return an "OK" (200) response.  We also include the number of milliseconds
    // since the program started running.
    // Note: This number will overflow (go back to zero), after approximately 50 days.
    server.send(200, "text/plain", "lights State Changed! (" + String(millis()) + ")");
  else
    server.send(200, "text/plain", "lights State Unchanged! (" + String(millis()) + ")");
}

// If the client requests any other URL than the root directory or the /setlights path:
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
  server.on("/setlights", HTTP_GET, handleSetlights);
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
