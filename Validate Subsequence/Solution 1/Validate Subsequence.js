function isValidSubsequence(array, sequence) {
  // Write your code here.
  let idx = 0
  for (let i = 0; i < array.length; i++) {
    if (idx === sequence.length) {
      break
    }
      if (array[i] === sequence[idx] && idx < sequence.length) {
        idx ++
      }
  }
  return idx === sequence.length
}


// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;

