const fs = require("fs");
const path = require("path");

const filePath = path.resolve(process.argv[2]);
const inputs = JSON.parse(process.argv[3]);
const source = fs.readFileSync(filePath, "utf8");
const isValid = new Function(`${source}\nreturn isValid;`)();

const results = inputs.map((value) => isValid(value));
process.stdout.write(JSON.stringify(results));
