const fs = require("fs");

const N = Number(fs.readFileSync("/dev/stdin").toString());
const nums = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((item) => +item);

let min = 1000000;
let max = -1000000;

for (let i = 0; i < N; i++) {
  if (min > nums[i]) {
    min = nums[i];
  }

  if (max < nums[i]) {
    max = nums[i];
  }
}

console.log(`${min} ${max}`);
