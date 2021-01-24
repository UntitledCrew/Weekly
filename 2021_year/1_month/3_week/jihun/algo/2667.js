let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n')

const N = +input[0]

const data = []

for (let i = 1; i < N+1; i++) {
    data.push(input[i].split('').map(el => (+el)))
}

const checked = new Array(N).fill(new Array(N).fill(0))

const dy = [1, 0, 0, -1]
const dx = [0, 1, -1, 0]

const bfs = function(sy, sx, cnt) {
    const queue = []
    queue.push([sy, sx])
    checked[sy][sx] = cnt
    while (queue) {
        const temp  = queue.pop()
        const y = temp[0]
        const x = temp[1]
        for (let i = 0; i < 4; i++) {
            const ny = y + dy[i]
            const nx = x + dx[i]
            if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                if (data[ny][nx] && !checked[ny][nx]) {
                    queue.push([ny, nx])
                    checked[ny][nx] = cnt
                }
            }
        }
    }
}

let cnt = 1
for (let y = 0; y < N; y++) {
    for (let x = 0; x < N; x++) {
        if (data[y][x] && !checked[y][x]) {
            bfs(y, x, cnt)
        }
    }
}