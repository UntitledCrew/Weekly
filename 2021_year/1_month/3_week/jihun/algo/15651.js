let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split(' ')

// const combination = function(depth) {
//     if (depth === M) {
//         answerString = answerString + answer.join(' ') + '\n'
//         return
//     }
//     for (let i = 1; i < N + 1; i++) {
//         answer.push(i)
//         combination(depth+1)
//         answer.pop(i)
//     }
// }

// const N = +input[0]
// const M = +input[1]

// const checked = new Array(N + 1).fill(false)

// const answer = []
// let answerString = ''
// combination(0)
// console.log(answerString.trim())


const combination = (lst, depth) => {
    if (depth === 1) {
        return lst.map(el => ([el]))
    }
    const answer = []
    lst.forEach((start, _, origin) => {
        const recursiveCombination = combination(origin, depth-1)
        const temp = recursiveCombination.map(el => [start, ...el])
        answer.push(...temp)
    })
    return answer
}

const N = +input[0]
const M = +input[1]

const nums = []
for (let i = 1; i < N+1; i++) {
    nums.push(i)
}

let answer = ''
combination(nums, M).forEach(comb => {
    answer = answer + comb.join(' ') + '\n'
})

console.log(answer)