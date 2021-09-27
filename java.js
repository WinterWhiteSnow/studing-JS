let dance = []

for(var i = 0; i < 10; i++){
	ob = {
		id:"id"+i,
		pw:"pw"+i
	}
   dance.push(ob);
}

for(var i = 0; i < 10; i++){
	console.log(dance[i]["pw"])
 }