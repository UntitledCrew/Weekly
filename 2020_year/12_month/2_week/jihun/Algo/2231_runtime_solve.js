let input = require('fs').readFileSync('./dev/stdin').toString().trim().split(' ');

let data = Number(input)

let answer = 0

for (let i = 0; i <= data; i++) {
    if (i === data) {
        answer = 0
        break
    }
    if (i + i.toString().split('').map(el => +el).reduce((acc, curr) => (acc + curr)) === data) {
        answer = i
        break
    }
}
console.log(answer)

// let num = 0
// while (num < data) {
//     if (num + num.toString().split('').map(el => +el).reduce((acc, curr) => (acc + curr)) === data) {
//         break
//     }
//     num++
// }
// console.log(num === data ? 0 : num)


// const recursive = function(current, depth) {
//     for (let i = 0; i < 10; i++) {
//         let targetNum
//         if (depth !== 0) {
//             targetNum = current.toString() + i.toString()
//         } else {
//             targetNum = i.toString()
//         }
//         let targetSum = targetNum.split('').map(target => Number(target)).reduce((acc, curr) => (acc + curr))
        
//         if (Number(targetNum) + targetSum === data) {
//             return Number(targetNum)
//         } else if (targetNum > data) {
//             return 0
//         }
//     }
//     return recursive(current+1, depth+1)
// }

// console.log(recursive(0, 0))