import subprocess
import sys

CLOSE_PAGE_PATH = "/usr/share/jitsi-meet/static/close3.html"
WATERMARK_IMG_PATH = "/usr/share/jitsi-meet/images/watermark.png"

CLOSE_PAGE_CONTENT = """
<html>     <head>         <style>             /*Global Variables*/ /*Colors*/ /*Box Size*/ /*Speed*/ /*Global Mixins*/ /*Global Spinner*/ .cp-spinner {   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   position: relative; } /*Round Spinner*/ .cp-round:before {   border-radius: 50%;   content: " ";   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 6px #bababa;   border-right: solid 6px #bababa;   border-bottom: solid 6px #bababa;   border-left: solid 6px #bababa;   position: absolute;   top: 0;   left: 0; } .cp-round:after {   border-radius: 50%;   content: " ";   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 6px #F56151;   border-right: solid 6px transparent;   border-bottom: solid 6px transparent;   border-left: solid 6px transparent;   position: absolute;   top: 0;   left: 0;   animation: cp-round-animate 1s ease-in-out infinite; } /*Round Spinner Animation*/ @keyframes cp-round-animate {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } } /*Pinwheel Spinner*/ .cp-pinwheel {   border-radius: 50%;   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 24px #0fd6ff;   border-right: solid 24px #58bd55;   border-bottom: solid 24px #eb68a1;   border-left: solid 24px #f3d53f;   animation: cp-pinwheel-animate 1s linear infinite; } /*Pinwheel Spinner Animation*/ @keyframes cp-pinwheel-animate {   0% {     border-top-color: #0fd6ff;     border-right-color: #58bd55;     border-bottom-color: #eb68a1;     border-left-color: #f3d53f;     transform: rotate(0deg);   }   25% {     border-top-color: #eb68a1;     border-right-color: #f3d53f;     border-bottom-color: #0fd6ff;     border-left-color: #58bd55;   }   50% {     border-top-color: #0fd6ff;     border-right-color: #58bd55;     border-bottom-color: #eb68a1;     border-left-color: #f3d53f;   }   75% {     border-top-color: #eb68a1;     border-right-color: #f3d53f;     border-bottom-color: #0fd6ff;     border-left-color: #58bd55;   }   100% {     border-top-color: #0fd6ff;     border-right-color: #58bd55;     border-bottom-color: #eb68a1;     border-left-color: #f3d53f;     transform: rotate(360deg);   } } /*Balls Spinner*/ .cp-balls {   animation: cp-balls-animate 1s linear infinite; } .cp-balls:before {   border-radius: 50%;   content: " ";   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background-color: #0fd6ff;   position: absolute;   top: 0;   left: 0;   animation: cp-balls-animate-before 1s ease-in-out infinite; } .cp-balls:after {   border-radius: 50%;   content: " ";   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background-color: #eb68a1;   position: absolute;   bottom: 0;   right: 0;   animation: cp-balls-animate-after 1s ease-in-out infinite; } /*Balls Spinner Animation*/ @keyframes cp-balls-animate {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } } @keyframes cp-balls-animate-before {   0% {     transform: translate(-5px, -5px);   }   50% {     transform: translate(0px, 0px);   }   100% {     transform: translate(-5px, -5px);   } } @keyframes cp-balls-animate-after {   0% {     transform: translate(5px, 5px);   }   50% {     transform: translate(0px, 0px);   }   100% {     transform: translate(5px, 5px);   } } /*Bubble Spinner*/ .cp-bubble {   border-radius: 50%;   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background: #58bd55;   animation: cp-bubble-animate 1s linear infinite; } .cp-bubble:before {   border-radius: 50%;   content: " ";   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background-color: #58bd55;   position: absolute;   left: -30px;   animation: cp-bubble-animate-before 1s ease-in-out infinite; } .cp-bubble:after {   border-radius: 50%;   content: " ";   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background-color: #58bd55;   position: absolute;   right: -30px;   animation: cp-bubble-animate-after 1s ease-in-out infinite; } /*Bubble Spinner Animation*/ @keyframes cp-bubble-animate {   0% {     opacity: 0.5;     transform: scale(1) translateX(0px);   }   25% {     opacity: 1;     transform: scale(1.1) translateX(-15px);   }   50% {     opacity: 1;     transform: scale(1.2) translateX(15px);   }   100% {     opacity: 0.5;     transform: scale(1) translateX(0px);   } } @keyframes cp-bubble-animate-before {   0% {     opacity: 0.5;     transform: scale(1);   }   25% {     transform: scale(1.1);   }   50%,   100% {     opacity: 1;     transform: scale(1);   } } @keyframes cp-bubble-animate-after {   0%,   50% {     opacity: 0.5;     transform: scale(1);   }   50% {     transform: scale(1.1);   }   75%,   100% {     opacity: 1;     transform: scale(1);   } } /*Flip Spinner*/ .cp-flip {   transform-style: preserve-3d;   perspective: 10em; } .cp-flip:before {   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   background: #F56151;   content: " ";   position: absolute;   top: 0;   left: 0;   animation: cp-flip-animate-before 2s linear infinite; } /*Flip Spinner Animation*/ @keyframes cp-flip-animate-before {   0% {     transform: rotateY(0deg) rotateX(0deg);   }   25% {     transform: rotateY(360deg) rotateX(0deg);   }   50% {     transform: rotateY(360deg) rotateX(360deg);   }   75% {     transform: rotateY(0deg) rotateX(360deg);   }   100% {     transform: rotateY(0deg) rotateX(0deg);   } } /*Hue Spinner*/ .cp-hue {   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background: #F56151;   border-radius: 50%;   animation: cp-hue-animate 1s ease-in-out infinite; } .cp-hue:before {   border-radius: 0% 12px 12px 0%;   content: " ";   width: 12px;   height: 24px;   display: inline-block;   box-sizing: border-box;   background: white;   position: absolute;   top: 0;   right: 0;   animation: cp-hue-animate-before 1s ease-in-out infinite; } /*Hue Spinner Animation*/ @keyframes cp-hue-animate {   0% {     background: #F56151;   }   25% {     background: #58bd55;   }   50% {     background: #eb68a1;   }   75% {     background: #f3d53f;   }   100% {     background: #F56151;   } } @keyframes cp-hue-animate-before {   0% {     transform: rotateY(0deg);     transform-origin: left center;     opacity: 0.5;   }   30%,   70% {     transform: rotateY(180deg);     transform-origin: left center;     opacity: 0.2;   }   100% {     transform: rotateY(0deg);     opacity: 0.5;   } } /*Skeleton Spinner*/ .cp-skeleton {   border-radius: 50%;   border-top: solid 6px #F56151;   border-right: solid 6px transparent;   border-bottom: solid 6px transparent;   border-left: solid 6px transparent;   animation: cp-skeleton-animate 1s linear infinite; } .cp-skeleton:before {   border-radius: 50%;   content: " ";   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 6px transparent;   border-right: solid 6px transparent;   border-bottom: solid 6px transparent;   border-left: solid 6px #F56151;   position: absolute;   top: -6px;   left: -6px;   transform: rotateZ(-30deg); } .cp-skeleton:after {   border-radius: 50%;   content: " ";   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 6px transparent;   border-right: solid 6px #F56151;   border-bottom: solid 6px transparent;   border-left: solid 6px transparent;   position: absolute;   top: -6px;   right: -6px;   transform: rotateZ(30deg); } /*Skeleton Spinner Animation*/ @keyframes cp-skeleton-animate {   0% {     transform: rotate(0deg);     opacity: 1;   }   50% {     opacity: 0.7;   }   100% {     transform: rotate(360deg);     opacity: 1;   } } /*Eclipse Spinner*/ .cp-eclipse {   width: 12px;   height: 12px;   display: inline-block;   box-sizing: border-box;   border-radius: 50%;   background: #f3d53f;   margin: 12px;   animation: cp-eclipse-animate 1s ease-out infinite; } .cp-eclipse:before {   border-radius: 50%;   content: " ";   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 6px transparent;   border-right: solid 6px #f3d53f;   border-bottom: solid 6px transparent;   border-left: solid 6px transparent;   position: absolute;   top: -18px;   left: -18px; } .cp-eclipse:after {   border-radius: 50%;   content: " ";   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   border-top: solid 6px transparent;   border-right: solid 6px transparent;   border-bottom: solid 6px transparent;   border-left: solid 6px #f3d53f;   position: absolute;   top: -18px;   right: -18px; } /*Eclipse Spinner Animation*/ @keyframes cp-eclipse-animate {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } } /*Boxes Spinner*/ .cp-boxes:before {   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   content: " ";   background: #58bd55;   position: absolute;   top: 12px;   left: 0;   animation: cp-boxes-animate-before 1s ease-in-out infinite; } .cp-boxes:after {   width: 24px;   height: 24px;   display: inline-block;   box-sizing: border-box;   content: " ";   background: #58bd55;   position: absolute;   top: 12px;   right: 0;   animation: cp-boxes-animate-after 1s ease-in-out infinite; } /*Boxes Spinner Animation*/ @keyframes cp-boxes-animate-before {   0% {     transform: translateX(-20px) rotate(45deg);   }   50% {     transform: translateX(-7px) rotate(225deg);   }   100% {     transform: translateX(-20px) rotate(45deg);   } } @keyframes cp-boxes-animate-after {   0% {     transform: translateX(20px) rotate(45deg);   }   50% {     transform: translateX(7px) rotate(-225deg);   }   100% {     transform: translateX(20px) rotate(45deg);   } } /*Morph Spinner*/ .cp-morph {   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box;   background: #0fd6ff;   animation: cp-morph-animate 1s linear infinite; } /*Morph Spinner Animation*/ @keyframes cp-morph-animate {   0% {     transform: rotate(0deg) scale(1);     border-radius: 0%;     background: #f3d53f;   }   25%,   75% {     transform: rotate(180deg) scale(0.4);     border-radius: 50%;     background: #0fd6ff;   }   100% {     transform: rotate(360deg) scale(1);     border-radius: 0%;     background: #f3d53f;   } } /*Heart Spinner*/ .cp-heart {   animation: cp-heart-animate 2s ease-in-out infinite; } .cp-heart:before {   border-radius: 12px 12px 0 0;   content: " ";   width: 24px;   height: 35px;   display: inline-block;   box-sizing: border-box;   background-color: #eb68a1;   transform: rotate(-45deg);   position: absolute;   top: 0;   left: 8px; } .cp-heart:after {   border-radius: 12px 12px 0 0;   content: " ";   width: 24px;   height: 35px;   display: inline-block;   box-sizing: border-box;   background-color: #eb68a1;   transform: rotate(45deg);   position: absolute;   top: 0;   right: 8px; } /*Heart Spinner Animation*/ @keyframes cp-heart-animate {   0% {     transform: scale(0.9);     transform-origin: center;   }   15% {     transform: scale(1.4);     transform-origin: center;   }   30% {     transform: scale(0.9);     transform-origin: center;   }   45% {     transform: scale(1.4);     transform-origin: center;   }   60%,   100% {     transform: scale(0.9);     transform-origin: center;   } } /*Meter Spinner*/ .cp-meter {   border-radius: 50%;   border-top: solid 6px #0fd6ff;   border-right: solid 6px #0fd6ff;   border-bottom: solid 6px #0fd6ff;   border-left: solid 6px #0fd6ff;   width: 48px;   height: 48px;   display: inline-block;   box-sizing: border-box; } .cp-meter:before {   border-radius: 3px;   content: " ";   width: 6px;   height: 12px;   display: inline-block;   box-sizing: border-box;   background-color: #0fd6ff;   position: absolute;   top: 5px;   left: 16px;   transform-origin: center bottom;   animation: cp-meter-animate-before 1s linear infinite; } /*Meter Spinner Animation*/ @keyframes cp-meter-animate-before {   0% {     transform: rotate(-45deg);   }   100% {     transform: rotate(315deg);   } } /*Spinners in Motion*/ .cp-wrapper {   text-align: center;   margin: 45px auto;   font-family: 'Roboto Condensed', sans-serif; } h1 {   color: #00ACC1;   font-size: 2.8em; } h1 span {   color: #00838F; } p {   color: #4a5b6c;   font-size: 1.2em; } p.credits {   font-size: 1em; } p.credits a {   margin: 0px; } a:link, a:active, a:visited {   color: #3F51B5;   text-decoration: none;   font-size: 1em;   text-transform: uppercase;   border-bottom: dashed 1px #3F51B5;   margin: 0px 10px; } a:hover {   border-bottom: none; } .cp-spinners {   margin: 10px auto; } .cp-spinner-block {   display: inline-block;   width: 40%;   margin: 40px 20px; } .cp-spinner-block span {   color: #4a5b6c;   display: block;   padding: 5px 0px; } .cp-spinner-block pre {   font-size: 0.75em;   background-color: #f0f0f0;   padding: 4px 7px;   border-radius: 2px;   font-family: "Lucida Console", Monaco, monospace;   display: inline-block;   white-space: pre-wrap; } @media only screen and (max-width: 1024px) {   .cp-wrapper {     width: 100%;   }   .cp-spinner-block {     display: block;     width: 90%;     margin: 40px 5%;   } } @media only screen and (min-width: 1025px) and (max-width: 1400px) {   .cp-wrapper {     width: 70%;   }   .cp-spinner-block {     margin: 40px auto;   } } @media only screen and (min-width: 1500px) {   .cp-wrapper {     width: 90%;   }   .cp-spinner-block {     display: inline-block;     width: 30%;     margin: 40px 20px;   } } @media only screen and (min-width: 1700px) {   .cp-wrapper {     width: 70%;   }   .cp-spinner-block {     display: inline-block;     width: 30%;     margin: 40px 20px;   } }          </style>     </head>     <body>          <div class="cp-wrapper" style="height: 100%;">             <div class="cp-spinners" style="height: 100%;">                 <div class="cp-spinner-block" style="height: 100%; width: 100%; display: flex; justify-content: center; align-items: center;">	                         <div class="cp-spinner cp-balls"></div>                 </div>             </div>         </div>     </body> </html>
"""
WATERMARK_IMG_DATAURL = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGP6zwAAAgcBApocMXEAAAAASUVORK5CYII="

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pybase64")

import base64 

png_recovered = base64.decodestring(WATERMARK_IMG_DATAURL.encode())
f = open(WATERMARK_IMG_PATH, "wb")
f.write(png_recovered)
f.close()




f = open(CLOSE_PAGE_PATH, "w")
f.write(CLOSE_PAGE_CONTENT)
f.close()



