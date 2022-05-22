let h1 = document.getElementById('heading1')
let number1 = document.getElementById('no1')
let number2 = document.getElementById('no2')
// main main

let optA = document.getElementById('add')
let optS = document.getElementById('sub')
let optM = document.getElementById('mul')
let optD = document.getElementById('div')
// ^^^ main vars

let x = parseInt(number1)
let y = parseInt(number2)
// main2 vars

var add = (x + y)
var sub = (x - y)
var div = (x / y)
var mul = (x * y)
var tap = (x ** y)
// extra vars

function checkeq(opt) {
	if (opt.value === "Add") {
		madd = True
	} else if (opt.value === "Subtract") {
		msub = True
	} else if (opt.value === "Div") {
		mdiv = True
	} else if (opt.value === "Multiply") {
		mmul = True
	} else if (opt.value === "And shit...") {
		mtap = True
	}
}
