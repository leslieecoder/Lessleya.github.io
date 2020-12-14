function selector() {
    let select = document.getElementById("selector").value;
    if (select == 'Payment') {
        function doPayment()
    } else {
        function doBalance()
    }
}

function doPayment() {
    /*Input*/
    let amountB = parseFloat(document.getElementById("amountB").value);
    let annualR = parseFloat(document.getElementById("annualR").value);
    let numberYears = parseFloat(document.getElementById("numberyears").value);
    let PerYear = parseFloat(document.getElementById("PerYear").value);

    //Process
    let payment = computePayment(amountB, annualR, numberYears, PerYear);
    let p = Payment.toFixed(2);

    //Output
    document.getElementById('output').innerHTML = '$' + p;
}

function computePayment(a, annualR, numYears, PerYear) {
    //process for calcuations
    let r = annualR / 12;
    let n = numberYears * PerYear;
    let f = a * Math.pow((1 + r), n);
    return f;
}

function doBalance() {
    //Input
    let amountBorrowed = parseFloat(document.getElementById("amountB").value);
    let annualRate = parseFloat(document.getElementById("annualR").value);
    let numOfYears = parseFloat(document.getElementById("numberYears").value);
    let periodsPerYear = parseFloat(document.getElementById("PerYear").value);

    //Process
    let Balance = computeBalance(amountB, annualR, numberYears, PerYear);
    let b = Balance.toFixed(2);

    //Output
    document.getElementById('output').innerHTML = '$' + b;
}

function computeBalance(a, annualR, numberYears, PerYear) {
    //process for the calcuations
    let r = annualR / 12;
    let n = numberYears * PerYear;
    let f = a * Math.pow((1 + r), n);
    return f;
}