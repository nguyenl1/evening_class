
// hello.addEventListener('click', function() {
//     alert('Hello World!');
//     // const task = document.getElementById('taskname').value;

//     // console.log(task)
// });


let mytasks = [] 

let form = document.querySelector("form");

form.addEventListener("submit", function(addtask) {
    console.log("Saving value", form.taskname.value);

    addtask.preventDefault();

    mytasks.push(form.taskname.value);

    console.log(mytasks)

    // let checkbox = document.createElement('input');
    // checkbox.type = "checkbox";
    // checkbox.name = "name";
    // checkbox.value = "value";
    // checkbox.id = "id";

    let tasklen = mytasks.length;

    let list = "<ul>";

    for (i = 0; i < tasklen; i++) {
        list += "<li>" + mytasks[i] + "</li>";
        
    }

    list += "</ul>";

    document.getElementById("listtasks").innerHTML = list; 

    

    document.forms[0].reset();

});

function complete() {

}

function removetask() {

}



