function addtacos() {
    // INPUT: Number of tacos.
    let number1 = document.getElementById("number1").value;
    let number2 = document.getElementById("number2").value;
    // PROCESSING: Add the number of tacos that yo and you friend can eat.
    //convert the string to numbers using parseFloat
    number1 = parseFloat(number1);
    number2 = parseFloat(number2);
    //add the two numbers together and stere in my output variable
    let sum = number1 + number2;
    // OUTPUT: Display how many tacos you and your friend can eat together.
    document.getElementById("output").innerHTML = "You should order " + sum + " <strong> tacos </strong> for you and your amigo🌮😃😃";
}