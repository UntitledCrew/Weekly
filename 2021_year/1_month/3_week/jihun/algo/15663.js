let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n')

const firstLine = input[0].split(' ').map(el => (+el))
const secondLine = input[1].split(' ').map(el => (+el))

// const combination = function(depth) {
//     if (depth === M) {
//         answerSet.add(answer.join(' '))
//         return
//     }
//     for (let i = 0; i < N; i++) {
//         if (!checked[i]) {
//             checked[i] = true
//             answer.push(nums[i])
//             combination(depth+1, nums[i])
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
// let answerSet = new Set()
// let answerString = ''
// combination(0)
// answerSet.forEach(answer => {
//     answerString = answerString + answer + '\n'
// })
// console.log(answerString.trim())



// 아래는 런타임
// const combination = (lst, depth) => {
//     if (depth === 1) {
//         return lst.map(el => ([el]))
//     }
//     const answer = new Set()
//     lst.forEach((start, index, origin) => {
//         const rest = origin.slice(0,index).concat(origin.slice(index+1,))
//         const recursiveCombination = combination(rest, depth-1)
//         // 왜 recursive가 set으로 바뀌지?
//         const temp = recursiveCombination.map(el => [start, ...el])
//         temp.forEach(el => {
//             answer.add(el.join(' '))
//         })
//     })
//     return answer
// }

// const N = firstLine[0]
// const M = firstLine[1]
// const nums = secondLine.sort((a, b) => (a - b))

// let answer = ''
// combination(nums, M).forEach(comb => {
//     answer = answer + comb + '\n'
// })

// console.log(answer.trim())


// set 사용 안하고
const combination = (depth) => {
    if (depth === M) {
        answerString = answerString + answer.join(' ') + '\n'
        return
    }
    for (let i = 0; i < keys.length; i++) {
        if (!count[i]) { continue }
        count[i]--
        answer[depth] = keys[i]
        combination(depth+1)
        count[i]++
    }
}

const N = firstLine[0]
const M = firstLine[1]
const nums = new Object()
secondLine.forEach(num => (nums[num] ? nums[num]++ : (nums[num] = 1)))

const keys = Object.keys(nums).map(el => (+el))
const count = Object.keys(nums).map(el => (nums[el]))

const answer = new Array(M).fill(false)
let answerString = ''
combination(0)

console.log(answerString)