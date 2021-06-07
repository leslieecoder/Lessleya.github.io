const hambutton = document.querySelector('.ham');
const mainnav = document.querySelector('.navigation')

hambutton.addEventListener('click', () => { mainnav.classList.toggle('responsive') }, false);

// To solve the mid resizing issue with responsive class on
window.onresize = () => { if (window.innerWidth > 760) mainnav.classList.remove('responsive') };

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

const imagesToLoad = document.querySelectorAll('img[data-src]');

//Optionla parameters being set for the IntersectionalObserver

const imgOptions = {
    threshold: 0,
    rootMargin: "0px 0px 50px 0px"
};

const loadImages = (image) => {
    image.setAttribute('src', image.getAttribute('data-src'));
    image.onload = () => { image.removeAttribute('data-src'); };
};

// first check to see if intersection Observer is supported

if ('IntersectionObserver' in window) {
    const imgObserver = new IntersectionObserver((items, imgObserver) => {
        items.forEach((item) => {
            if (item.isIntersecting) {
                loadImages(item.target);
                imgObserver.unobserve(item.target);
            }
        });
    }, imgOptions);

    //Loop through each img an check status and Load if necessary    
    imagesToLoad.forEach((img) => {
        imgObserver.observe(img);
    });
} else {
    imagesToLoad.forEach((img) => {
        loadImages(img);
    });
}