let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

let count = input[0];
let data = [];

for (let i = 1; i < input.length; i++) {
    if (input[i] !== '') {
        data.push(input[i].split(' '));
    }
}

let answer = []
for (let i = 0; i < count; i++) {
    let result = 0
    let targetKg = Number(data[i][0])
    let targetTall = Number(data[i][1])

    
    for (let j = 0; j < count; j++) {
        if (i !== j) {
            let compareTargetKg = Number(data[j][0])
            let compareTargetTall = Number(data[j][1])
            if (targetKg < compareTargetKg && targetTall < compareTargetTall) {
                result++
            }
        }
    }
    answer.push(result+1)
}
console.log(answer.join(' '))

