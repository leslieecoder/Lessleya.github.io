function fixedLoops() {

    /*Loop Number1 */
    let out1 = " ";
    let i = 0;
    while (i < 2) {
        out1 += `Part 1:${i}<br>`;
        i += 1;
    }

    /*Loop Number 2*/
    let out2 = " ";
    for (let j = 0; j < 3; j++) {
        if (j !== 2) {
            out2 += `Part 2:${j}, `;
        } else {
            out2 += `Part 2:${j}`;
        }
    }
    /*Loop Number 2*/
    let out3 = " ";
    for (let k = 0; k < 4; k++) {
        out3 += k + " ";
    }

    /*Loop Number 2*/
    let balance = 1000;
    const rate = .10;
    let n = 30;
    for (let s = 0; s < n; s++) {
        let interest = balance * rate;
        balance += interest;
    }

    /*
     * let i = 0;
     * while (i < 3); {
     *   i++; }
     * The i++; shoud inside the while parethesis */

    /*Outputs*/
    document.getElementById('output1').innerHTML = out1;
    document.getElementById('output2').textContent = out2;
    document.getElementById('output3').textContent = out3;
    document.getElementById('output4').textContent = balance;
}