#!/usr/bin/env python

#Two pics animation

import time

man1 = r"""
     .  .      
      \/       
     (@@)      
  g/\_)(_/\e   
 g/\(=--=)/\e   
     //\\      
    _|  |_ 
"""

man2 = r"""
     .  .      
      \/       
  g\ (@@) /e     
 g\ \_)(_/ /e  
   \(=--=)/   
     //\\      
    _|  |_    
"""

while True:
    # Clear the screen
    print("\033c", end="")

    # Display pic
    print(man1)

    # Swap the pics
    man1, man2 = man2, man1

    # Time between swaps
    time.sleep(0.5)

