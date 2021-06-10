async function getDadJoke() {
    const url = 'https://icanhazdadjoke.com/';
    let h = new Headers({
        Accept: 'application/json',
        'User-Agent': 'WDD-230-Test User Agent https://ahfxadam.github.io/'
    });

    const response = await fetch(url, { headers: h1 });

    if (response.status = 200) {
        return response.json();
    } else {
        throw new Error('No dad jokes found: ' + response.status);

    }

    function newJoke() {
        const dad_id = document.getElelmentById('dad-joke');
        dad_id.innerHTML = '';
        const joke = getDadJoke().then(function(j) {

            let joke = j['joke']
            dad_id.innerHTML = joke;
        });
    }

}