let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

let [N, M, V] = input[0].split(' ').map(el => +el);
let flag = []
let edge = []
let check = []

for (let i = 0; i < N; i++) {
    flag.push(0)
}

for (let i = 0; i < N+1; i++) {
    let temp = []
    let temp2 = []
    for (let j = 0; j < N+1; j++) {
        temp.push(0)
        temp2.push(0)
    }
    edge.push(temp)
    check.push(temp2)
}

for (let i = 1; i < M+1; i++) {
    let [node1, node2] = input[i].split(' ').map(el => +el)
    edge[node1][node2] = 1
    edge[node2][node1] = 1
}

let dfsAnswer = []
const dfs = function(n, v) {
    if (flag.every(node => node === 1)) {
        return
    }
    if (flag[v-1] === 0) {
        flag[v-1] = 1
        dfsAnswer.push(v)
    }
    for (let i = 1; i < n+1; i++) {
        if (edge[v][i] === 1 && check[v][i] !== 1) {
            check[v][i] = 1
            dfs(n, i)
        }
    }
}
dfs(N, V)
console.log(dfsAnswer)
