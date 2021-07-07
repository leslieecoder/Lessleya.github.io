/*Hamburguer Button*/

const hambutton = document.querySelector('.ham');
const mainnav = document.querySelector('.navigation')

hambutton.addEventListener('click', () => { mainnav.classList.toggle('responsive') }, false);

// To solve the mid resizing issue with responsive class on
window.onresize = () => { if (window.innerWidth > 760) mainnav.classList.remove('responsive') };

/*pancakes*/
let date = new Date();
let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

let currentMonth = months[date.getMonth()]
let currentDay = days[date.getDay()]
let currentYear = date.getFullYear()


document.getElementById("currentDate").innerHTML = date = `${currentDay}, ${currentMonth} ${currentYear}`;

const pancakes = document.getElementById("pancakes")

if (currentDay === "Friday") {
    pancakes.className = "pancakes-show"

} else {
    pancakes.className = "pancakes-hidden"
}

/*Windchill*/

var temp = document.getElementById("temp");
var t = temp.textContent;
var windSpeed = document.getElementById("windspeed");
var s = windSpeed.textContent;
document.getElementById
if (t <= 50 && s > 3.0) {
    var f = (0.0817 * (3.71 * (Math.pow(s, 0.5)) +
        5.81 - 0.25 * s) * (t - 91.4) + 91.4);;
    var n = f.toFixed(2);
    document.getElementById("windChill").innerHTML = n;
    console.log(n);
} else {
    document.getElementById("windChill").innerHTML = "N/A";
}
console.log(t);