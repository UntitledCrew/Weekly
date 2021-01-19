let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split(' ')

const combination = function(depth, s) {
    if (depth === M) {
        answerString = answerString + answer.join(' ') + '\n'
        return
    }
    for (let i = s; i < N + 1; i++) {
        if (!checked[i]) {
            checked[i] = true
            answer.push(i)
            combination(depth+1, i)
            answer.pop(i)
            checked[i] = false
        }

    }
}

const N = +input[0]
const M = +input[1]

const checked = new Array(N + 1).fill(false)

const answer = []
let answerString = ''
combination(0, 1)
console.log(answerString.trim())


// const combination = (lst, depth) => {
//     if (depth === 1) {
//         return lst.map(el => ([el]))
//     }
//     const answer = []
//     lst.forEach((start, index, origin) => {
//         // const rest = origin.slice(0, index).concat(origin.slice(index+1,))
//         const rest = origin.slice(index+1,)
//         const recursiveCombination = combination(rest, depth-1)
//         const temp = recursiveCombination.map(el => [start, ...el])
//         answer.push(...temp)
//     })
//     return answer
// }

// const N = +input[0]
// const M = +input[1]

// const nums = []
// for (let i = 1; i < N+1; i++) {
//     nums.push(i)
// }

// combination(nums, M).forEach(comb => {
//     console.log(comb.join(' '))
// })