let dance = []

for(var i = 0; i < 10; i++){
	ob = {
		id:i,
		pw:i
	}
   dance.push(ob);
}

for(var i = 0; i < 10; i++){
	document.write(dance[i]["pw"])
	console.log(1 == dance[i]["id"],i)
	if (1 == dance[i]["id"]){
		console.log("들어가있어요")
		break
	}
	else{
		console.log("없어요")
	}
 }

// document.write(dance["id"])