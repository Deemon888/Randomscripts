let h1 = document.getElementById('heading1')
let no1 = document.getElementById('no1')
let no2 = document.getElementById('no2')
// main vars

let b1 = document.getElementById('button1')
const opts = document.querySelector('#operations')
// imp vars

let x = parseInt(no1)
let y = parseInt(no2)
// ex vars

b1.addEvenetListener('click', e => {
	if (opts.value === 'add') {
		h1.innerHTML = x + ' + ' + y + ' = ' + (x + y)
	} else if (opts.value === 'sub') {
		h1.innerHTML = x + ' - ' + y + ' = ' + (x - y)
	} else if (opts.value === 'mul') {
		h1.innerHTML = x + ' x ' + y + ' = ' + (x * y)
	} else if (opts.value === 'div') {
		h1.innerHTML = x + ' / ' + y + ' = ' + (x / y)
	}
});
