import Foundation

// Set the URL the request is being made to.
let request = URLRequest(url: NSURL(string: "http://192.168.43.247/setblinds?blinds=STOP")! as URL)
do {
    // Perform the request
    var response: AutoreleasingUnsafeMutablePointer<URLResponse?>? = nil
    let data = try NSURLConnection.sendSynchronousRequest(request, returning: response)
    
    // Convert the data to JSON
    let jsonSerialized = try JSONSerialization.jsonObject(with: data, options: []) as? [String : Any]
    
    if let json = jsonSerialized, let url = json["url"], let explanation = json["explanation"] {
        print(url)
        print(explanation)
    }
}


print("I WORKED!")
