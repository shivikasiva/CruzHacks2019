//
//  SignUpViewController.swift
//  CruzHacks2019
//
//  Created by Srilekha Vutukuru on 1/19/19.
//  Copyright © 2019 Srilekha Vutukuru. All rights reserved.
//

import UIKit
import Firebase
import Foundation
import FirebaseAuth

class SignUpViewController: UIViewController{

    
  
    @IBOutlet weak var usernameField: UITextField!
    @IBOutlet weak var emailField: UITextField!
    @IBOutlet weak var passwordField: UITextField!
    @IBOutlet weak var password2Field: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
     //   FirebaseApp.configure()
        // Do any additional setup after loading the view.
    }
    

    
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    
    @IBAction func createUser(_ sender: UIButton) {
        let username : String? = "temp"//usernameField.text else {return}
        let email : String? = "vutukurusrilekha@gmail.com"//emailField.text else {return}
        let pass : String? = "cruzhacks1"//passwordField.text else {return}
        let pass2 : String? = "cruzhacks1"//password2Field.text else {return}
        //guard let username = usernameField.text, !username.isEmpty else {print ("Username is empty"); return}
        //guard let email = emailField.text, !email.isEmpty else {print ("Email is empty"); return}
        //guard let pass = passwordField.text, !pass.isEmpty else {print ("Password is empty"); return}
        //guard let pass2 = password2Field.text, !pass2.isEmpty else {print ("Password 2 is empty"); return}
        Auth.auth().createUser(withEmail: email!, password: pass! ){ user, error in
            if error == nil && user != nil{
                if pass == pass2{
                    
                    print ("You are registered")
                }
            }
            else{
                print ("regestration failed")
            }
        }
    }
    
}
