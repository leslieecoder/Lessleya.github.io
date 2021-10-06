console.log(typeof 42);
console.log(typeof "abc");
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof { "a": 1 });
console.log(typeof [1, 2, 3]);
console.log(typeof
    function hello() {});

var adult = false;
let age = 24;
const PROFFESION = 'Instructor'

if (adult) {
    var myName = "Bob";
}

console.log(myName);
// Bob

console.log(age);
// Error!

console.log(PROFFESION);

adult = parseInt('20') - 3; //or use Number()

console.log(adult);

let myVariable = 6;

myVariable = 6;

console.log(myVariable);


document.getElementById('p2').textContent = "Hello World";
document.querySelector('#p2').textContent = "Thisis it.";

document.querySelector('.p3').innerText = "This is is a class selector";


document.querySelector('p').innerText = "Which one?";

document.querySelectorAll('p')[0].innerText = "Which one";