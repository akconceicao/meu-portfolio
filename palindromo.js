function palindromo(palavra) {
  if (palavra.length < 3) return "?";

  for (let i = 0; i < Math.floor(palavra.length / 2); i++) {
    if (palavra[i] !== palavra[palavra.length - 1 - i]) {
      return "N";
    }
  }

  return "S";
}

// Testes
console.log(palindromo("")); // "?"
console.log(palindromo("anilina")); // "S"
console.log(palindromo("mama")); // "N"
console.log(palindromo("mm")); // "?"
