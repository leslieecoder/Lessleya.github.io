function myCalculator() {
    //INPUT: Get two number and one basic operator from the user.
    let number1 = document.getElementById("number1").value;
    let operator = document.getElementById("operator").value;
    let number2 = document.getElementById("number2").value;
    let answer = document.getElementById("answer").value;

    //PROCESSING: convert the string to numbers using parseFloat
    number1 = parseFloat(number1);
    number2 = parseFloat(number2);
    answer = parseFloat(answer);
    //assign the message acording the process and answer

    let correct;

    if (operator == '+') {

        correct = number1 + number2;

    } else if (operator == '-') {

        correct = number1 - number2;

    } else if (operator == "*") {

        correct = number1 * number2;

    } else {

        correct = number1 / number2;

    }

    // Compare answer that was given to the correct answer 

    if (answer == correct) {

        document.getElementById('output').innerHTML = "Correct🏆";

    } else {

        document.getElementById('output').innerHTML = "Incorrect😢";

    }

}