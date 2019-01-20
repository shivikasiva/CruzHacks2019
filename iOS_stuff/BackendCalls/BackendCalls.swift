//
//  BackendCalls.swift
//  CruzHacks2019
//
//  Created by Srilekha Vutukuru on 1/20/19.
//  Copyright © 2019 Srilekha Vutukuru. All rights reserved.
//

import Foundation

class BackendCalls {
    
    class func lightSwitch(_ switchValue: Bool ) {
        // Set the URL the request is being made to.
        let switchString = switchValue ? "ON":"OFF"
        let request = URLRequest(url: NSURL(string: "http://192.168.43.115/setlights?lights=\(switchString)")! as URL)
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
        } catch {
            print("Backend Calls", error)
        }
        
        
        print("I WORKED!")
    }
    
    class func blinds(_ switchValue: Bool ) {
        // Set the URL the request is being made to.
        let switchString = switchValue ? "DOWN":"STOP"
        let request = URLRequest(url: NSURL(string: "http://http://192.168.43.247/setblinds?blinds=\(switchString)")! as URL)
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
        } catch {
            print("Backend Calls", error)
        }
        
        
        print("I WORKED!")
    }
    
    class func calender() {
        
        // Set the URL the request is being made to.
        let request = URLRequest(url: NSURL(string: "http://192.168.43.237:5000/")! as URL)
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
        catch {
            print("Backend Calls", error)
        }
        
        
        print("I WORKED!")
    }
    
}

