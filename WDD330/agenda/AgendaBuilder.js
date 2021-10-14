export default class AgendaBuilder {
    constructor(dataPath) {
        this.dataPath = dataPath;
        this.data = {};

    }
    async init() {
        await this.getData();
        console.log(this.data);
    }

    async getData() {
        try {
            const response = await fetch(this.dataPath)
        }
        this.data = await fetch(this.dataPath).then(response = response.json())
    })
renderTracks(tracks) {}
this.dataPath
renderCourses(courses) {}

}