const apiURL = "https://api.openweathermap.org/data/2.5/weather?id=5604473&appid=a1ae1eb12eb3ea4848cc295aeda6d43d&units=imperial";
fetch(apiURL)
    .then((response) => response.json())
    .then((jsObject) => {
        console.log(jsObject);
        document.getElementById('weather').textContent = jsObject.weather[0].main;
        document.getElementById('temp').textContent = jsObject.main.temp_max;
        document.getElementById('humidity').textContent = jsObject.main.humidity;
        document.getElementById('windspeed').textContent = jsObject.wind.speed;

    });



const forecast = "https://api.openweathermap.org/data/2.5/forecast?id=5604473&appid=a1ae1eb12eb3ea4848cc295aeda6d43d&units=imperial";
fetch(forecast)
    .then((response) => response.json())
    .then((jsObject) => {
        const weatherTitle = document.getElementById("weatherTitle");
        const weatherData = document.getElementById("weatherData")
        weatherData.innerHTML = '';
        console.log(jsObject);
        for (var i = 0; i < jsObject.list.length; i++) {
            if (jsObject.list[i].dt_txt.includes("18:00:00")) {
                weatherData.innerHTML += `<td> <img src="https://openweathermap.org/img/wn/${jsObject.list[i].weather[0].icon}@2x.png">
                                            ${jsObject.list[i].main.temp} °F
                                        </td>`;

                let date = new Date(jsObject.list[i].dt * 1000);
                let day = date.getDay();

                switch (day) {
                    case 0:
                        day = "Sunday";
                        break;
                    case 1:
                        day = "Monday";
                        break;
                    case 2:
                        day = "Tuesday";
                        break;
                    case 3:
                        day = "Wednesday";
                        break;
                    case 4:
                        day = "Thursday";
                        break;
                    case 5:
                        day = "Friday";
                        break;
                    case 6:
                        day = "Saturday";
                        break;
                }

                weatherTitle.innerHTML += `<th> ${day}</th>`
            }
        }
    });

const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
    .then(function(response) {
        return response.json();
    })
    .then(function(jsonObject) {
        console.table(jsonObject);


        const events = jsonObject.towns[0].events;

        let card = document.createElement('section');
        let event0 = document.createElement('p');
        let event1 = document.createElement('p');
        let event2 = document.createElement('p');



        event0.textContent = events[0];
        event1.textContent = events[1];
        event2.textContent = events[2];

        card.appendChild(event0);
        card.appendChild(event1);
        card.appendChild(event2);

        document.querySelector('div.upcoming-event').appendChild(card);
    });