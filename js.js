loginForm.style.marginRight=`${inputId.scrollWidth/2+30}px`;
submitButton.style.height=`${inputId.offsetHeight+inputPW.offsetHeight}px`;
loginButton.style.height=`${inputId.offsetHeight+inputPW.offsetHeight}px`;
title.style.color = "white";
title.style.fontSize = "40px";
count.style.color = "white";
const clickNumber = "clickNumber";
const userInfo = "userinfo"

let userList=[]
const saveUserList = JSON.parse(localStorage.getItem(userInfo))
if(saveUserList) {
	userList = saveUserList
}

let game = 0;
const save = parseInt(localStorage.getItem(clickNumber));
if (save) {
	game = save;
}

function saveNumber(){
	localStorage.setItem(clickNumber,game);
}

function saveUser(){
	localStorage.setItem(userInfo,JSON.stringify(userList))
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

function sign(event){
	event.preventDefault();
	const id = inputId.value;
	const pw = inputPW.value;
	savelist = {
		id:id,
		pw:pw,
		usercode:Date.now()
	}
	inputId.value=""
	inputPW.value=""
	userList.push(savelist)
	saveUser()
}

function findUser(apple) {
    return apple === true;
}

function findUser2(banana){
	return banana === false;
}
let response = []
function login(event){
	event.preventDefault()
	if (userList.length>0){
		for (let i = 0; i<userList.length; i++){
			if (loginID.value == userList[i]["id"] && loginPW.value == userList[i]["pw"])
			{return response.push(true)}
			else{
				return response.push(false)
			}
		}
	}
	else{
		return response.push(undefined)
	}
	console.log(response)
	loginID.value=""
	loginPW.value=""
	if (response.find(findUser)){
		alert("환영합니다!")
	}
	else if (response.find(findUser2)){
		alert("으잉")
	}
	else{
		alert(response)
	}
}







signForm.addEventListener("submit",sign)
loginForm.addEventListener("submit",login)
window.addEventListener("click", clickClick)

setInterval(making, 100);