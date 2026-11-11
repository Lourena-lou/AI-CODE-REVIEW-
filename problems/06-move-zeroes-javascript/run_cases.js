const fs = require("fs");
const path = require("path");

const filePath = path.resolve(process.argv[2]);
const inputs = JSON.parse(process.argv[3]);
const source = fs.readFileSync(filePath, "utf8");
const moveZeroes = new Function(`${source}\nreturn moveZeroes;`)();

const results = inputs.map((value) => {
  const copy = value.slice();
  moveZeroes(copy);
  return copy;
});
process.stdout.write(JSON.stringify(results));
