let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n')

const firstLine = input[0].split(' ').map(el => (+el))
const secondLine = input[1].split(' ').map(el => (+el))

// const combination = function(depth) {
//     if (depth === M) {
//         answerString = answerString + answer.join(' ') + '\n'
//         return
//     }
//     for (let i = 0; i < N; i++) {
//         if (!checked[i]) {
//             checked[i] = true
//             answer.push(nums[i])
//             combination(depth+1)
//             answer.pop(nums[i])
//             checked[i] = false
//         }
//     }
// }

// const N = firstLine[0]
// const M = firstLine[1]
// const nums = secondLine.sort((a, b) => (a - b))

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
    lst.forEach((start, index, origin) => {
        const rest = origin.slice(0, index).concat(origin.slice(index+1,))
        const recursiveCombination = combination(rest, depth-1)
        const temp = recursiveCombination.map(el => [start, ...el])
        answer.push(...temp)
    })
    return answer
}

const N = firstLine[0]
const M = firstLine[1]
const nums = secondLine.sort((a, b) => (a - b))

let answer = ''
combination(nums, M).forEach(comb => {
    answer = answer + comb.join(' ') + '\n'
})

console.log(answer)