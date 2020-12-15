let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

let N = input[0].split(' ')[0];
let M = input[0].split(' ')[1];
let data = [];

let startW = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
let startB = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

for (let i = 1; i < input.length; i++) {
    if (input[i] !== '') {
        data.push(input[i].split(' '))
    }
}

let answer = 987654321
for (let x = 0; x < M; x++) {
    let tempAnswer = 0
    if (x+8 <= M) {
        for (let y = 0; y < N; y++) {
            let tempAnswerW = 0
            let tempAnswerB = 0
            if (y+8 <= N) {
                console.log(y, x)
                for (let z = 0; z < 8; z++) {
                    let target = data[y+z][0].slice(x, x+8).split('')
                    target.forEach((wb, index) => {
                        if (y+z % 2) {
                            if (wb !== startW[index]) {
                                tempAnswerW++
                            }
                            if (wb !== startB[index]) {
                                tempAnswerB++
                            }
                        } else {
                            if (wb !== startB[index]) {
                                tempAnswerW++
                            }
                            if (wb !== startW[index]) {
                                tempAnswerB++
                            }
                        }
                    })
                }
                tempAnswer = tempAnswerB > tempAnswerW ? tempAnswerW : tempAnswerB
                if (tempAnswer < answer) {
                    answer = tempAnswer
                }
            }
        }
    }
}

console.log(answer)


```
10 10
WWBBWWWBBW
WBBWBWWWWB
WBWBWWBBWW
WBBBBBBBWW
WBBWWWBWWW
WBBBBBWWBB
WWBWWBWWBB
BWWBBWWWBB
BBWBBBBBWB
WWWBBBWWWB




8 8
WBWBWWBB
WBBBBBBB
WBBWWWBW
WBBBBBWW
WWBWWBWW
BWWBBWWW
BBWBBBBB
WWWBBBWW
```