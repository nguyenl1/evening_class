
// hello.addEventListener('click', function() {
//     alert('Hello World!');
//     // const task = document.getElementById('taskname').value;

//     // console.log(task)
// });


let mytasks = [] 

let form = document.querySelector("form");

form.addEventListener("submit", function(event) {
    console.log("Saving value", form.taskname.value);

    event.preventDefault();

    mytasks.push(form.taskname.value);

    let ul = document.getElementById("listtasks").innerHTML=mytasks;
    document.forms[0].reset();
    
});


function removetask() {

}

function complete() {

}

function main() {

}
