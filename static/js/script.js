// create set time out function to clear aler messages after 2 seconds
"use strict";
setTimeout(() => {
   const element=document.getElementById('msg') ;
   if(element){element.remove() ;
   }
 }, 5000);