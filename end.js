// const hellow = document.getElementsByClassName("wow")
const hellow = document.querySelectorAll(".wow")
for (let i = 0; i<hellow.length;i++){
	if (i>1){
		hellow[i].innerText="hello"+i;
	}
	else{
		hellow[i].innerText="not hello"+i;
	}
}

const a = ["a","false","Yes","no",undefined,true,"true"]

function findCherries(fruit) {
	if (fruit === true){return true;}
    else if (fruit === "false"){return false;}
	else {return undefined;}
}

console.log(a.find(findCherries));