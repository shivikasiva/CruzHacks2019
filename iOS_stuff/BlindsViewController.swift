//
//  BlindsViewController.swift
//  CruzHacks2019
//
//  Created by Srilekha Vutukuru on 1/20/19.
//  Copyright © 2019 Srilekha Vutukuru. All rights reserved.
//

import UIKit

class BlindsViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    
    @IBAction func DOWN(_ sender: Any) {
        BackendCalls.blinds(true)
    }
    
    @IBAction func STOP(_ sender: Any) {
        BackendCalls.blinds(false)
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
