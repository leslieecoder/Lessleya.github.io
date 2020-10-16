function convKg() {


    //INPUT:  Read a pounds number from the user.
    let pounds = document.getElementById("pounds").value;
    //PROCESSING convert the string to numbers using parseFloat
    pounds = parseFloat(pounds);
    //Convert the number of pounds into Kilograms by dividing pounds / 2.205
    let kilos = pounds / 2.205;


    //OUTPUT: Display the number of kilograms

    document.getElementById("output").innerHTML = pounds + " <strong> pounds </strong> equal to " + kilos.toFixed(1) + "<strong> kilos👩🏻‍💻</strong>.";
}