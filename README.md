# LFSR & Berlekamp-Massey algorithm
<div>
  <!-- Stability -->
  <a href="https://nodejs.org/api/documentation.html#documentation_stability_index">
    <img src="https://img.shields.io/badge/stability-experimental-orange.svg?style=flat-square"
      alt="API stability" />
  </a>
  <!-- Standard -->
  <a href="https://img.shields.io/badge">
    <img src="https://img.shields.io/badge/Language-Python-brightgreen.svg"
      alt="Python" />
  </a>
</div>
<br />

Python implementation of LFSR and Berlekamp-Massey algorithm.

## Example

```sh
TEST - LFSR & Berlekamp-Massey

################################## Encryption ##################################

Cleartext       : the secret is: there is no spoon
LFSR init       : x^6 + x^5 + x^1 + 1 (000101)
LFSR stream     : 1745d1745d1745d1745d1745d1745d1745d1745d1745d1745d1745d1745d1745
Ciphertext      : 632db4542e7226a31129372ca24e7d632db40638372ca254337865a20432782b

################################## Decryption ##################################

Known cleartext : the
Stream start    : 1745d1
Recovered LFSR  : x^6 + x^5 + x^1 + 1
LFSR stream     : 1745d1745d1745d1745d1745d1745d1745d1745d1745d1745d1745d1745d1745

Decrypted       : the secret is: there is no spoon

##################################### Test #####################################

Test OK         : True
```

