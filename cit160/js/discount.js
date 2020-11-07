/* Input: customer's subtotal

       * Processing: if subtotal > $50 && today is Tuesday or Wednesday, subtract 10% from the subtotal.

       * Output: Total amount due by adding sales tax of 6% to the subtotal.

       */

function disCount() {

    //Assign Variables

    const salesTax = .06;

    const discount = .1;

    let totalPrice = 0;

    let discountAmount = 0;

    let taxAmount = 0;

    let findDiscount = 0;







    //Input

    var dayOfWeek = new Date().getDay(); // interger

    console.log("Day of week: " + dayOfWeek)

    let subtotal = parseFloat(document.getElementById("subtotal").value);



    //Processing      

    if (subtotal > 50 && (dayOfWeek == 2 ^ dayOfWeek == 3)) {

        findDiscount = (subtotal * discount);

        discountAmount = subtotal - findDiscount;

        taxAmount = discountAmount * salesTax;

        totalPrice = taxAmount + discountAmount;

    } else {

        totalPrice = subtotal + (salesTax * subtotal);

    }

    // Output

    document.getElementById("output").textContent = totalPrice.toFixed(2);

}