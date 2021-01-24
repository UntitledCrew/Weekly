let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n')

const firstLine = input[0].split(' ').map(el => (+el))
const secondLine = input[1].split(' ').map(el => (+el))

const combination = function(depth) {
    if (depth === M) {
        answerSet.add(answer.join(' '))
        return
    }
    for (let i = 0; i < N; i++) {
        answer.push(nums[i])
        combination(depth+1)
        answer.pop(nums[i])
    }
}

const N = firstLine[0]
const M = firstLine[1]
const nums = secondLine.sort((a, b) => (a - b))

const checked = new Array(N + 1).fill(false)

const answer = []
let answerSet = new Set()
let answerString = ''
combination(0)
answerSet.forEach(answer => {
    answerString = answerString + answer + '\n'
})
console.log(answerString.trim())



// 아래는 런타임, 안풀어봄, 풀어보기
// const combination = (lst, depth) => {
//     if (depth === 1) {
//         return lst.map(el => ([el]))
//     }
//     const answerSet = new Set()
//     lst.forEach((start, index, origin) => {
//         const rest = origin.slice(index+1,)
//         const recursiveCombination = combination(rest, depth-1)
//         const temp = recursiveCombination.map(el => [start, ...el])
//         temp.forEach(el => {
//             return answerSet.add(el.join(' '))
//         })
//     })
//     return answerSet
// }

// const N = firstLine[0]
// const M = firstLine[1]
// const nums = secondLine.sort((a, b) => (a - b))

// let answer = ''
// combination(nums, M).forEach(comb => {
//     return answer = answer + comb + '\n'
// })

// console.log(answer.trim())