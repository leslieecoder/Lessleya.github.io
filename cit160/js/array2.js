/* Defining Table
      Input: No user input.
      Process: Test the countEvens and multiply functions
      Output: The values returned from the countEvens and multiply functions.
     */
function test() {
    let list1 = [17, 8, 9, 5, 20];
    let list2 = [12, 4, 8, 15, 17, 5, 20, 11];

    /* Test the countEvens function by calling it two times*/
    let count1 = countEvens(list1);
    let count2 = countEvens(list2);

    /* Test the multiply function by calling it two times */
    let times1 = multiply(list1, 3);
    let times2 = multiply(list2, 2);

    /* Build a string to display to the user*/
    let output =
        count1 + '<br>' +
        count2 + '<br>' +
        times1 + '<br>' +
        times2;

    // Display the output string for the user to see.
    document.getElementById('output').innerHTML = output;
}

function countEvens(list) {
    /*
     * Input: array of numbers
     * Processing: If even add 1 to count
     * Output: count
     */

    //Processing:
    let count = 0;
    for (let index in list) {
        if (list[index] % 2 == 0) { count++; }
    }

    //Output:
    return count;
}

function multiply(list, multiplier) {
    /*
     * Input:array of numbers, multiplier
     * Processing: copy list and Multiply each element in the array by the multiplier
     * Output: productionList
     */

    //Processing:
    let productList = [...list];
    for (let index in productList) {
        productList[index] *= multiplier;
    }

    //Output:
    return productList;
}