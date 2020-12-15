let input = require('fs').readFileSync('./dev/stdin').toString().trim().split(' ');

let data = Number(input)

const recursive = function(current, depth) {
    for (let i = 0; i < 10; i++) {
        let targetNum
        if (depth !== 0) {
            targetNum = current.toString() + i.toString()
        } else {
            targetNum = i.toString()
        }
        let targetSum = targetNum.split('').map(target => Number(target)).reduce((acc, curr) => (acc + curr))
        
        if (Number(targetNum) + targetSum === data) {
            return Number(targetNum)
        } else if (targetNum > data) {
            return 0
        }
    }
    return recursive(current+1, depth+1)
}

console.log(recursive(0, 0))