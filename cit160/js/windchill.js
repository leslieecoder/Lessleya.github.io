 /*
  * Input: tempF, speed as Float
  * Processing: run windChill()
  * Output: chill
  */

 //Javascript Code Here
 function doInputOutput() {
     //Input:
     let tempF = parseFloat(document.getElementById('temperature').value);
     let speed = parseFloat(document.getElementById('windSpeed').value);

     //Processing:
     let chill = windChill(tempF, speed)

     //Output:
     document.getElementById('output').innerHTML = chill;
 }

 function windChill(tempF, speed) {
     /*
      * Input: tempF, speed as Float
      * Processing, Output: (35.74 + 0.6215 * tempF) - (35.75 * (speed ** 0.16)) + (0.4275 * tempF * (speed ** 0.16))
      */
     //Output:
     return (35.74 + 0.6215 * tempF) - (35.75 * (speed ** 0.16)) + (0.4275 * tempF * (speed ** 0.16))
 }