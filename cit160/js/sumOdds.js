function sumOdds() {
    let inte = parseInt(document.getElementById("inte").value);

    let sum = 0;
    for (i = 1; i <= inte; i += 2) {
        sum += i;
    }
    document.getElementById("output").innerHTML = sum;
}