const title = document.querySelector("header");
const body = document.querySelector("body");
const count = document.querySelector("h4.count");
const main = document.querySelector("main.login");
const inputId = document.querySelector(".id");
const inputPW = document.querySelector(".passward");
const submitButton = document.querySelector(".submit");
const form = document.querySelector(".login-form")


main.style.marginRight=`${inputId.scrollWidth/2+30}px`;
submitButton.style.height=`${inputId.offsetHeight+inputPW.offsetHeight}px`;
title.style.color = "white";
title.style.fontSize = "40px";
count.style.color = "white";
const clickNumber = "clickNumber";

let userList=[]

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
		body.style.backgroundColor = "red";
	}
	else{
		body.style.backgroundColor = "blue";
	}
	game+=1
	saveNumber();
}

function refresh () {
	location.reload(true);
}

function making() {
	count.innerText = `${game}`;
	body.style.backgroundColor = "#A5DE9F";
	// const span = document.createElement("span");
	// span.innerText = "wow";
	// title.appendChild(span)
	// console.log(window.outerWidth);
}

function login(event){
	event.preventDefault();
	const id = inputId.value;
	const pw = inputPW.value;
	ob = {
		id:id,
		pw:pw,
		usercode:Date.now()
	}
	inputId.value=""
	inputPW.value=""
	userList.push(ob)
	console.log(userList)
	
}
form.addEventListener("submit",login)
window.addEventListener("click", clickClick)

setInterval(making, 100);