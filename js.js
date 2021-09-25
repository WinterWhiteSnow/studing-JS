const title = document.querySelector("header")

title.style.color = "white";
title.style.fontSize = "40px";
const clickNumber = "clickNumber";

let game = 0;
const save = parseInt(localStorage.getItem(clickNumber,game));
if (save) {
	game = save;
}

function saveNumber(){
	localStorage.setItem(clickNumber,game);
}

function clickClick() {	
	game+=1
	saveNumber();
	location.reload(true);
}

const span = document.createElement("span");
span.innerText = game;
title.appendChild(span)

window.addEventListener("click", clickClick)