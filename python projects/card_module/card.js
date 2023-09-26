
// Approach
// steps 1
/* 
render the amount of input container in the render container */

let contNumber = document.getElementById("contNumber")
const renderBtn = document.getElementById("render-button")
let fightersInput = document.getElementById("fightersInput")
function renderInputContainer() {
    renderBtn.addEventListener("click",()=>{
        console.log("button is working")
        if (contNumber.value > 0) {
            fightersInput.value = contNumber.value  
                for (let i = 0; i < inputArr.length; i++) {
                    fightersInput.innerHTML += inputArr[i]; 
                }
            } 
                 else {
            contNumber.value ="your render container has no value"
          }
    } );
};

renderInputContainer()