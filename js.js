const title = document.querySelector("header")
const body = document.querySelector("body")
const count = document.querySelector("h4.count")

title.style.color = "white";
title.style.fontSize = "40px";
count.style.color = "white";
const clickNumber = "clickNumber";

let game = 0;
const save = parseInt(localStorage.getItem(clickNumber,game));
if (save) {
	game = save;
}

function saveNumber(){
	localStorage.setItem(clickNumber,game);
}

function clickClick(event) {
	const X = event.x;
	const screenX = window.outerWidth;
	
	if (screenX/2 > X) {
		body.style.backgroundColor = "green";
		console.log("short!")
	}
	else{
		body.style.backgroundColor = "grey";
		console.log("long!")
	}
	game+=1
	saveNumber();
}

function refresh () {
	location.reload(true);
}

function making() {
	// const span = document.createElement("span");
	count.innerText = `${game}`;
	body.style.backgroundColor = "black";
	// title.appendChild(span)
	console.log("why");
}

window.addEventListener("click", clickClick)
setInterval(making, 1000);