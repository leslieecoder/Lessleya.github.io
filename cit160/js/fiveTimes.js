function fiveTimes() {
    let table = "";

    for (initial = 1; initial <= 12; initial++) {
        let multiplier = 5;
        let result = 5 * initial;

        table += multiplier + " * " + initial + " = " + result + "<br>";
    }
    document.getElementById("output").innerHTML = table;
}