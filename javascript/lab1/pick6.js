const readline = require('readline-sync');

//let userInput = parseInt(readline.question('enter a number: '));
//console.log(`you entered: {${userInput}`);

function pick6(){
    let x = 0;
    let y = [];
    while (true){
        let ran = Math.floor((Math.random() *100) + 1 );
        x = x + 1;
        y.push(ran);

        if (x === 6){
            return y 
            
        }


    }
    
}

let comp = pick6()
let yours = pick6()

function num_matches(comp,yours){
    let range = [0,1,2,3,4,5];
    let match = 0;
    var i; 
    for (i in range) {
        if (yours[i] == comp[i]){
            match += 1;
        }
        else {
            match += 0;
        }
        return match;
    }


}

// console.log(comp)
// console.log(yours)
// console.log(num_matches(comp,yours))

function balance(match){
    let balance = 0;
    let new_balance = balance - 2;
    if (match == 0){
        new_balance += 0;
    } else if (match == 1) {
        new_balance += 4;
    }
    else if (match == 2) {
        new_balance += 7;
    }
    else if (match == 3) {
        new_balance += 100;
    }
    else if (match == 4) {
        new_balance += 50000;
    }
    else if (match == 5) {
        new_balance += 1000000;
    }
    else if (match == 6) {
        new_balance += 25000000;
    }
    return new_balance
}

// console.log(balance(num_matches(comp,yours)))


function compare () {
    let x = 0
    let current_balance = 0
    while (true) {
        x += 1;
        comp = pick6();
        yours = pick6();

        current_balance = current_balance + balance(num_matches(comp,yours));

        console.log('Winning Ticket: ' + comp );
        console.log('Your Ticket: ' + yours );


        if (x == 10) {
            break;
        }
        
    }
    console.log('Your balance is: $' + current_balance)

}

console.log(compare())