document.getElementById("demo").innerHTML="Hello World!";

const task = document.getElementById('taskname');

task.oninput = function() {
    console.log('user entered some text: '+task.value);
};


// var todo = document.getElementsByTagName("ul"); 