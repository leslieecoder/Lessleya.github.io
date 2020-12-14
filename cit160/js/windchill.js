 /*
  * Input: tempF, speed as Float
  * Processing: run windChill()
  * Output: chill
  */

 function doInputOutput() {
     /*Input*/
     let temperature = parseFloat(document.getElementById("temperature").value);
     let windspeed = parseFloat(document.getElementById("windspeed").value);
     let text = " ";
     let f;

     /*Process*/
     if (windspeed < 3) {
         text = "The windspeed is low";
     } else if (temperature > 50)
         text = "The temperature is high";
     else {
         f = windChill(temperature, windspeed)
     }

     /*Output*/
     document.getElementById('output1').innerHTML = f;
     document.getElementById('output2').innerHTML = text;
 }

 function windChill(temperature, windspeed) {
     f = 35.42 + (0.6215 * temperature) - (35.75 * windspeed ** 0.16) + (0.4275 * temperature *
         windspeed ** 0.16)
     return f;
 }