#Meisje

a simple project re-implement [Roger Johansson's idea](http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/)

the original image is:
![alt tag](https://raw.githubusercontent.com/zhy0216/Meisjie/master/sample.png)

the process of evolve:
![alt tag](https://raw.githubusercontent.com/zhy0216/Meisjie/master/animated.gif)

##Extra note:
speed up: process the video  
https://support.apple.com/kb/PH2239?locale=en_US

how to record screen  
http://osxdaily.com/2010/11/16/screen-recorder-mac/ 

use ImageMagick to generate gif:

`python sequence.py > sequence.txt`  
`convert -delay 20 -loop 0 @sequence.txt animated.gif`