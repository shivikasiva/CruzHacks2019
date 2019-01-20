//
//  LoginViewController.swift
//  
//
//  Created by Srilekha Vutukuru on 1/19/19.
//

import UIKit
import Firebase

class LoginViewController: UIViewController {

    @IBOutlet weak var emailField: UITextField!
    
    @IBOutlet weak var passwordField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    

    
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    
    @IBAction func loginFunc(_ sender: Any) {
        let email = "vutukurusrilekha@gmail.com"//emailField.text
        let pass = "cruzhacks1"//passwordField.text
        Auth.auth().signIn(withEmail: email, password: pass){ user, error in
            if error==nil && user != nil{
                print ("logged in ")
                //self.dismiss(animated: false, completion: nil)
            }
            else{
                print ("Error in logging in")
            }
        }
    }
    
 

}
