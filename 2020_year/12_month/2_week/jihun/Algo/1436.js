let input = require('fs').readFileSync('./dev/stdin').toString().trim().split(' ');

let data = Number(input)

let count = 0
let num = 666
let answer = 0
while (count != data) {
    if (num.toString().indexOf('666') !== -1) {
        count++
        answer = num
    }
    num++
}
console.log(answer)