function isValid(s) {
  let round = 0;
  let square = 0;
  let curly = 0;
  for (const ch of s) {
    if (ch === "(") round += 1;
    else if (ch === ")") round -= 1;
    else if (ch === "[") square += 1;
    else if (ch === "]") square -= 1;
    else if (ch === "{") curly += 1;
    else if (ch === "}") curly -= 1;
    if (round < 0 || square < 0 || curly < 0) return false;
  }
  return round === 0 && square === 0 && curly === 0;
}
