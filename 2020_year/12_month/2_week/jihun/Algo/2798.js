let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

let [N, M] = input[0].split(' ');
let cards = input[1].split(' ').map(el => +el).sort((a,b) => (a - b))
let answer = 0
cards.forEach(card1 => {
    if (card1 <= M) {
        cards.filter(card => card !== card1).forEach(card2 => {
            if (card1 + card2 <= M && card1 <= card2) {
                cards.filter(card => card !== card2).forEach(card3 => {
                    let cardSum = card1 + card2 + card3
                    if (cardSum <= M && card2 <= card3) {
                        if (cardSum > answer) {
                            answer = cardSum
                        }
                    }
                })
            }
        })
    }
})

console.log(answer)

// let answer = 0
// const combination = function(source, target, n, r, count, m) {
//     const sums = target.reduce((acc, curr) => (acc + curr))
//     if (sums > m) {
//         return
//     }
//     if (r === 0) {
//         if (sums <= m && answer < sums) {
//             answer = sums
//         }
//         return
//     } else if(n === 0 || n < r) {
//         return
//     } else {
//         target.push(source[count])
//         combination(source, [...target], n - 1, r - 1, count + 1, m)
//         target.pop()
//         combination(source, [...target], n - 1, r, count + 1, m)
//     }
// }

// combination(cards, [0], N, 3, 0, M)
// console.log(answer)
