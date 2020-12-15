let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

let [N, M] = input[0].split(' ');
let cards = input[1].split(' ').map(el => +el).sort((a,b) => (a - b))
let answer = 0
const combination = function(source, target, n, r, count, m) {
    const sums = target.reduce((acc, curr) => (acc + curr))
    if (sums > m) {
        return
    }
    if (r === 0) {
        if (sums <= m && answer < sums) {
            answer = sums
        }
        return
    } else if(n === 0 || n < r) {
        return
    } else {
        target.push(source[count])
        combination(source, [...target], n - 1, r - 1, count + 1, m)
        target.pop()
        combination(source, [...target], n - 1, r, count + 1, m)
    }
}

combination(cards, [0], N, 3, 0, M)
console.log(answer)
