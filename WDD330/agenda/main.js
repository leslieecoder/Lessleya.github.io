/*

build agenda data
fetch agenda data
render track info 

convert time to local time zone
render out classes 
style

*/

import AgendaBuilder
from "./AgendaBuilder";

const agenda = new AgendaBuilder('agenda.json');
agenda.init()

const today = new Date();