const readline = require('readline-sync');

/*let userInput1 = parseInt(readline.question('Enter the units: '));

let userInput2 = readline.question('Enter the ft, mi, km, yd, in: ');

if (userInput2 == 'ft') {
    let answer = userInput1 * 0.3048
    console.log(answer + " meters");
} else if (userInput2 == 'mi') {
    let answer = userInput1 * 1609.34
    console.log(answer+ " meters");
} else if (userInput2 == 'km') {
    let answer = userInput1 * 1000
    console.log(answer + " meters")
} else if (userInput2 == 'yd') {
    let answer = userInput1 * 0.9144
    console.log(answer + "meters")
} else if (userInput2 == 'in') {
    let answer = userInput1 * 0.0254
    console.log(answer + "meters")
}else {
    console.log("invalid response")
}
*/

let meters = {
    feet: 0.3048,
    miles: 1609.34,
    meters: 1,
    kilo: 1000,
    yard: 0.9144,
    inch: 0.0254
};
let distance = parseFloat(readline.question('Enter the distance: '));

let from_units = meters.get(readline.question('Enter your measurement in feet, miles, meters, kilo, yard, or inch. '));

let userInput3 = meters.get(readline.question('Enter your measurement you would like to ocnvert to in feet, miles, meters, kilo, yard, or inch. '));

let measure = (distance * from_units) / to_units

console.log(measure)