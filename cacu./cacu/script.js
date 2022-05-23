// input
let FirstInput = document.getElementById("no1");
let SeconeInput = document.getElementById("no2");

// result cont
let resultCont = document.getElementById("result");

// operations
let operations = document.getElementById("operation");

operations.addEventListener("change", () => {
  if (FirstInput.value != "" && SeconeInput.value != "") {
    let x = parseInt(FirstInput.value);
    let y = parseInt(SeconeInput.value);

    switch (operations.value) {
      case "":
        resultCont.innerHTML = `Calculate...`;
        FirstInput.value = "";
        SeconeInput.value = "";
        break;
      case "add":
        resultCont.innerHTML = `Answer: ${x + y}`;
        break;
      case "sub":
        resultCont.innerHTML = `Answer: ${x - y}`;
        break;
      case "div":
        resultCont.innerHTML = `Answer: ${x / y}`;
        break;
      case "mul":
        resultCont.innerHTML = `Answer: ${x * y}`;
        break;
    }
  } else {
    resultCont.innerHTML = "Pleas fill up some umbers to continue";
    operations.value = "";
  }
});
