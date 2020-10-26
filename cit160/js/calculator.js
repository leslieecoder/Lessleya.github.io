function myCalculator() {
    //INPUT: Get two number and one basic operator from the user.
    let number1 = document.getElementById("number1").value;
    let operator = document.getElementById("operator").value;
    let number2 = document.getElementById("number2").value;
    let answer = document.getElementById("answer").value;

    //PROCESSING: convert the string to numbers using parseFloat
    number1 = parseFloat(number1);
    number2 = parseFloat(number2);
    operator = parseFloat(operator);
    answer = parseFloat(answer);
    //assign the message acording the process and answer

    let correct = false;
    let output = 'Incorrect 😢';
    switch (operator) {
        case '+':
            if ((number1 + number2) == answer) {
                correct = true;
            }
            break;
        case '-':
            if ((number1 - number2) == answer) {
                correct = true;
            }
            break;
        case '*':
            if ((number1 * number2) == answer) {
                correct = true;
            }
            break;
        case '/':
            if ((number1 / number2) == answer) {
                correct = true;
            }
            break;
        default:
            break;
    }
    if (correct) {
        output = 'Correct🏆';
    }
    document.getElementById('output').innerHTML = output;
}