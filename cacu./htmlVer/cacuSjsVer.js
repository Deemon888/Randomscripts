let h1 = document.getElementById('heading1')
let number1 = document.getElementById('no1')
let number2 = document.getElementById('no2')
let b1 = document.getElementById('button1')
// main main

let optA = document.getElementById('add')
let optS = document.getElementById('sub')
let optM = document.getElementById('mul')
let optD = document.getElementById('div')
//
let opc = [optA, optS, optM, optD]
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
// functions

b1.addEventListen('keypress', function event() {
	checkeq(opc)
	if (madd === True) {
		h1.innerText = x + ' + ' + y + ' = ' add
	} else if (msub === True) {
		h1.innerText = x + ' - ' + y + ' = ' sub
	} else if (mdiv === True) {
		h1.innerText = x + ' / ' + y + ' = ' div
	} else if (mmul === True) {
		h1.innerText = x + ' x ' + y + ' = ' mul
	}
})
// button
