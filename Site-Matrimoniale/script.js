/*
//var list = [10, 100, 'sdada', true];

//var array = new Array(10, 100, 'sdada', true);

//var a = array[2];
//console.log(a);

//schimba indexu
//array[3] = false;
//console.log(array);
//console.log(array, list);
/*
var list = [1, 2, 3, 44];
console.log(list);

list.push(1,2,'hello');
console.log(list);

for (var z = 0; z<=3; z++){
	sters = list.pop();
	console.log(sters);
}
console.log(list);
*/
/*
var Alex   = new Array(8, 9, 7);
var Andrei = new Array(10, 11, 9);
var Adrian = new Array(11, 10, 4);

if (Andrei[0] > Adrian[0] && Adrian[0] > Alex[0]){
	console.log('Andrei e primu, Adrian pe doi si Alex pe trei');
}
else if(Andrei[1]>Adrian[1] && Adrian[1]>Alex[1]){
	console.log('Andrei e primu, Adrian pe doua si Alex pe trei');
	console.log(Andrei[1] + ' ' + Adrian[1] + ' '+ Alex[1]);
}
else if(Andrei[2]>Adrian[2] && Adrian[2]>Alex[2]){
	console.log('Andrei e primu, Adrian pe doua si Alex pe trei');
	console.log(Andrei[2] + ' ' + Adrian[2] + ' '+ Alex[2]);
}
*/
//DE REVENIT CAND AFLI CUM FUNCTIONEAZA INPUTU!!!!!!!!!!!!!!!!!!!


/*
var list= new Array(1,2,3,4,5,6);
console.log(list);
list.splice(2, 0,  10, 20, 30);
console.log(list);

//splice(index de inceput, cate elemente vrei sa stergi, daca vrei sa adaugi ceva);

list.splice(2, 3);
console.log(list);
//
list.splice(3, 2, 100, 200);
console.log(list);
*/
//let aray = new Array(7, 2, 3, 4, 5, 6 ,7);
/*
var count = 0;
var array = new Array(7, 4, 10);

for (var i=0; i < array.length; ++i){
	count++;
	console.log(count);
}

//console.log(count);
*/
/*
function getSecondLargest(nums){
	var array = [];
	//array.push(nums);

//var z = array.sort();

	console.log(array.sort());
	let z = array.length-2;
	console.log(array[z]);
	
	for (let e of array){
		array.push(nums)
	}
	console.log(array);
}
getSecondLargest(2, 3, 6, 6, 5);
*/
/*
function reverseString(s) {
    var splitString = s.split(""); // var splitString = "hello".split("");
    // ["h", "e", "l", "l", "o"]
 
    var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
    // ["o", "l", "l", "e", "h"]
 
    var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
    // "olleh"
	try {
		/*
		var splitString = s.split(""); // var splitString = "hello".split("");
    // ["h", "e", "l", "l", "o"]
 
    var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
    // ["o", "l", "l", "e", "h"]
 
    var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
    // "olleh"
	}
	*/
	/*
	catch (ex){
		console.log(ex.message);
	}
    return joinArray; // "olleh"
}
 
console.log(reverseString());
*/
/*
function computer(drive, ram, cpu){
	this.drive = drive;
	this.ram   = ram;
	this.cpu   = cpu;
}

var mynewcomp = new computer ('hard','3gb', 'intel');
*/
/*
var list = [[1, 2, 3], [4, 5, 6], [7, 8, 9,0]];
console.log(list);
console.log(list[1][2]);
console.log(list[2][0]);
list[2][3] = 10;
console.log(list);
*/
/*
var a = new Object();
//console.log(a);

a.name = 'George';
a.age = 100;
a.secondName = 'Muresan';
a.city = 'Cluj-Napoca';
a.friends = ('A', 'B', 'C');
a.NUME = function(x, y){
	return x+ " " + y;
}
console.log(a.NUME(a.name,a.secondName));
console.log(a.city);
console.log(a['city']);
//console.log(a);
*/
/*
var user = {
	name: 'George',
	score: 100,
	country: 'Romania',
	pets: ['Thea', 'Thea2', 'Thea3'],
	profile: {
		type: 'private',
		account: 'premium'
	}
};
if ('name' in user){
	console.log('User has a profile');
}
console.log(user.photo);

//console.log(user);
//console.log(user.country);
//console.log(user.pets[2]);
//console.log(user.profile.account);
*/