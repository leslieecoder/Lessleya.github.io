/*
 * Input: principal, annualRate, years, periodsPerYear
 * Processing: computeFutureValue()
 * Output: futureValue
 */

//Javascript Code Here
function doFV() {
    //Input:
    let principal = parseFloat(document.getElementById('principal').value);
    let annualRate = parseFloat(document.getElementById('annualRate').value);
    let years = parseInt(document.getElementById('years').value);
    let periodsPerYear = parseInt(document.getElementById('periodsPerYear').value);

    //Processing/Output:
    document.getElementById('futureValue').innerHTML = "$" + computeFutureValue(principal, annualRate, years, periodsPerYear).toFixed(2);

}

function computeFutureValue(principal, annualRate, years, periodsPerYear) {
    //Processing/Output:
    let futureValue = principal * (1 + annualRate / periodsPerYear) ** (years * periodsPerYear);
    futureValue = Math.round(futureValue * 100) / 100;

    return futureValue;
}