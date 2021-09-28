loginForm.style.marginRight=`${inputId.scrollWidth/2+30}px`;
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

function sign(event){
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
}

function login(){
	if (userList.length>0){
		for (let i = 0; i<userList.length; i++){
			if (inputId.value === userList[i]["id"])
			{console.log("wow")}
			else{
				console.log(userList[i]["id"],"wowwow");
			}
		}
	}
	else{
		alert("회원정보가 없습니다, 가입을 완료하세요.")
	}
}

signForm.addEventListener("submit",sign)
loginForm.addEventListener("submit",login)
window.addEventListener("click", clickClick)

setInterval(making, 100);