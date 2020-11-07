function sleepIn() {

    var now = new Date();

    var month = now.getMonth();

    var dayOfMonth = now.getDate();

    var dayOfWeek = now.getDay();

    if (month == 0 && dayOfMonth == 1) {

        document.getElementById("output").innerHTML = "Yesss! You can sleep in🛌🏽🛌🏽";

    } else if (month == 6 && dayOfMonth == 4) {

        document.getElementById("output").innerHTML = "Yesss! You can sleep in🛌🏽🛌🏽";

    } else if (month == 11 && dayOfMonth == 25) {

        document.getElementById("output").innerHTML = "Yesss! You can sleep in🛌🏽🛌🏽";

    } else if (dayOfWeek == 0 ^ dayOfWeek == 6) {

        document.getElementById("output").innerHTML = "Yesss! You can sleep in🛌🏽🛌🏽";

    } else {

        document.getElementById("output").innerHTML = "Nuh nuh get Up!🤸🏼 🤸🏼‍♂️";

    }

}