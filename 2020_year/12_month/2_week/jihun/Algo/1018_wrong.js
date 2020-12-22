let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

let N = input[0].split(' ')[0];
let M = input[0].split(' ')[1];
let data = [];

// let startW = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
// let startB = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

let startW = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]
let startB = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]


for (let i = 1; i < input.length; i++) {
    if (input[i] !== '') {
        data.push(input[i].split(''))
    }
}


let answer = 987654321
for (let y = 0; y < N; y++) {
    if (y+8 <= N) {
        for (let x = 0; x < M; x++) {
            let tempAnswerW = 0
            let tempAnswerB = 0
            if (x+8 <= M) {
                console.log(y, x)
                for (let i = 0; i < 8; i++) {
                    for (let j = 0; j < 8; j++) {
                        if (i % 2) {
                            if (data[y+i][x+j] !== startB[i][j]) {
                                tempAnswerB++
                            }
                            if (data[y+i][x+j] !== startW[i][j]) {
                                tempAnswerW++
                            }
                        } else {
                            if (data[y+i][x+j] !== startW[i][j]) {
                                tempAnswerB++
                            }
                            if (data[y+i][x+j] !== startB[i][j]) {
                                tempAnswerW++
                            }
                        }
                    }
                }
                let minAnswer = tempAnswerB > tempAnswerW ? tempAnswerW : tempAnswerB
                if (minAnswer < answer) {
                    answer = minAnswer
                }
            }
        }
    }
}

console.log(answer)


// ```
// 10 10
// WWBBWWWBBW
// WBBWBWWWWB
// WBWBWWBBWW
// WBBBBBBBWW
// WBBWWWBWWW
// WBBBBBWWBB
// WWBWWBWWBB
// BWWBBWWWBB
// BBWBBBBBWB
// WWWBBBWWWB




// 8 8
// WBWBWWBB
// WBBBBBBB
// WBBWWWBW
// WBBBBBWW
// WWBWWBWW
// BWWBBWWW
// BBWBBBBB
// WWWBBBWW
// ```