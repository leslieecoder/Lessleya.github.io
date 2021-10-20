let currentDate = new Date();

let today;

today = today.getDate();

let message;

if (dayOfWeek >= 1 && dayOfWeek <= 5) {
    message1 = "Hang in there!";
}

if (dayOfWeek >= 1 && dayOfWeek <= 5) {
    message1 = "Hang in there!";
} else {
    message1 = "Woohoo!  It is the weekend!";
}

let message;

switch (dayOfWeek) {
    case 0:
        message2 = "Sunday";
        break;
    case 1:
        message2 = "Monday";
        break;
    case 2:
        message2 = "Tuesday";
        break;
    case 3:
        message2 = "Wednesday";
        break;
    case 4:
        message2 = "Thursday";
        break;
    case 5:
        message2 = "Friday";
        break;
    case 6:
        message2 = "Saturday";
        break;
    default:
        message2 = "Unknown - " + dayOfWeek;
        break;
}

document.querySelector("#message1").textContent = message1;

document.querySelector("#message2").textContent = message2;

let templeList = [];

const output = (temples) => {
    temples.forEach((temple) => {
        let article = document.createElement("article");

        let templeName = document.createElement("h3");
        templeName.textContent = temple.templeName;

        let location = document.createElement("h4");
        location.textContent = temple.location;

        let dedicated = document.createElement("h4");
        dedicated.textContent = temple.dedicated;

        let img = document.createElement("img");
        img.setAttribute("src", temple.imageUrl);
        img.setAttribute("alt", temple.templeName);

        article.appendChild(templeName);
        article.appendChild(location);
        article.appendChild(dedicated);
        article.appendChild(img);

        document.querySelector("#temples").appendChild(article);
    });
};

fetch("https://byui-cse.github.io/cse121b-course/week05/temples.json")
    .then((response) => response.json())
    .then((temples) => {
        templeList = temples;
        output(templeList);
    });

const reset = () => {
    document.querySelector("#temples").innerHTML = "";
};

const sortBy = () => {
    reset();

    let filter = document.querySelector("#sortBy").value;

    switch (filter) {
        case "templeNameAscending":
            output(
                templeList.sort((temple1, temple2) => {
                    let templeName1 = temple1.templeName.toLowerCase();
                    let templeName2 = temple2.templeName.toLowerCase();
                    if (templeName1 < templeName2) return -1;
                    else if (templeName1 > templeName2) return 1;
                    else return 0;
                })
            );
            break;
        case "templeNameDescending":
            output(
                templeList.sort((temple1, temple2) => {
                    let templeName1 = temple1.templeName.toLowerCase();
                    let templeName2 = temple2.templeName.toLowerCase();
                    if (templeName1 > templeName2) return -1;
                    else if (templeName1 < templeName2) return 1;
                    else return 0;
                })
            );
            break;
        default:
            // using ternary operators
            output(
                templeList.sort((temple1, temple2) =>
                    temple1.templeName.toLowerCase() > temple2.templeName.toLowerCase() ?
                    1 :
                    temple2.templeName.toLowerCase() >
                    temple1.templeName.toLowerCase() ?
                    -1 :
                    0
                )
            );
            break;
    }
};

document.querySelector("#sortBy").addEventListener("change", sortBy);