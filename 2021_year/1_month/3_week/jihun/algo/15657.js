let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n')

const firstLine = input[0].split(' ').map(el => (+el))
const secondLine = input[1].split(' ').map(el => (+el))

const combination = function(depth, s) {
    if (depth === M) {
        answerString = answerString + answer.join(' ') + '\n'
        return
    }
    for (let i = nums.indexOf(s); i < N; i++) {
        answer.push(nums[i])
        combination(depth+1, nums[i])
        answer.pop(nums[i])
    }
}

const N = firstLine[0]
const M = firstLine[1]
const nums = secondLine.sort((a, b) => (a - b))

const answer = []
let answerString = ''
combination(0, nums[0])
console.log(answerString.trim())


// const combination = (lst, depth) => {
//     if (depth === 1) {
//         return lst.map(el => ([el]))
//     }
//     const answer = []
//     lst.forEach((start, index, origin) => {
//         const rest = origin.slice(index,)
//         const recursiveCombination = combination(rest, depth-1)
//         const temp = recursiveCombination.map(el => [start, ...el])
//         answer.push(...temp)
//     })
//     return answer
// }

// const N = firstLine[0]
// const M = firstLine[1]
// const nums = secondLine.sort((a, b) => (a - b))

// let answer = ''
// combination(nums, M).forEach(comb => {
//     answer = answer + comb.join(' ') + '\n'
// })

// console.log(answer)