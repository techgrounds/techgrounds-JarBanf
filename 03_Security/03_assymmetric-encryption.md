# Assymetric encryption
Asymmetric encryption, also known as public-key cryptography, is a type of encryption that uses a pair of keys to encrypt and decrypt data. The pair of keys include a public key, which can be shared with anyone, and a private key, which is kept secret by the owner. In asymmetric encryption, the sender uses the recipient's public key to encrypt the data. The recipient then uses their private key to decrypt the data.  
This approach allows for secure communication between two parties without the need for both parties to have the same secret key.

## Key-terms


## Assignment
1. Generate a key pair.
2. Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key. The recipient should be able to read the message, but it should remain a secret to everyone else. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the difference between this method and symmetric encryption.

### Used sources
- [What is Asymmetric Encryption?](https://www.geeksforgeeks.org/what-is-asymmetric-encryption/)
- [Online RSA Encryption, Decryption And Key Generator Tool(Free)](https://www.devglan.com/online-tools/rsa-encryption-decryption)

### Encountered problems
None

### Result
**1. Generate a key pair.**

My Public Key:

```bash
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCBmY5DFgvuLaZoFhBPTLk8C2kQ3EIgFUhByg+DDpVq/5wPPz1RG703eJGoNjYtdY0z3oltpMAKBkW+YeIGcOtplV3mqvJAlWBSJ6hUbwnLfppoeouyeJqsWqrvbJaOZ0Fxkl7zkZSMElVqmgcZAElw8rIngrM/NXmDKwl0WDjjeQIDAQAB
```

<br>
My Private Key:  

```bash
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAIGZjkMWC+4tpmgWEE9MuTwLaRDcQiAVSEHKD4MOlWr/nA8/PVEbvTd4kag2Ni11jTPeiW2kwAoGRb5h4gZw62mVXeaq8kCVYFInqFRvCct+mmh6i7J4mqxaqu9slo5nQXGSXvORlIwSVWqaBxkASXDysieCsz81eYMrCXRYOON5AgMBAAECgYBuYOMqPfexRo4I7mm7sGO/QRSd+IoVGyssZTTq8RvPQp6e2cSWdOKmAPlFY86mzwyRFcLEcGHi5860xFcmFzxXu7jY4ZuEP4BNq1igfH190LPtZkRDUFgCc1EeSuAd4qng4BVLaVYi5Uv+ke5dYFdqeDz2SGoJGY7Rhv6DAf/lhQJBAMlvfbI/C795V4oUyyhQ1mm5eR9FvTVyjSP+OiTCz4qg7kB/JLTUnXSuICxabn+gmJ51IWzc1K2ghJLvkl7GC8sCQQCktKHXSUGZdusUD3ic/2c+6OWDYOHau1G+xiC6AQvziYhVPD2MSHt+qwww6yQKFCZSmVroyvwDfkLTviB5ym1LAkEApJxLp8IFo69RbjGX45ZL4ZID/R5MhMTbujIi6a+ZUrw4dtRv9qZZFeTFvfkYm4ttrPAjJIdB9bFbJYhJoNFPCQJAECoqOBbYeVdSewWJsN7gIyx4WgyIHg+EVlTboWW45o3482SWJc53UFc5OxPY1aRknnaulWpWkYEyzdU7GrjjQQJAP2DeO/wuywI4A5/kSV5YZSrtqdmGhIhX71C2ah30okyGfwOKMr+sc1/AXZCGpuAKav/G7okZ8xtYDo6kJIkxaA==
```

![my public and private key](/03_Security/images/03_assymmetric-encryption1.png)<br><br>

**2. Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key. The recipient should be able to read the message, but it should remain a secret to everyone else. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the difference between this method and symmetric encryption.**

- Step1: One of my peers sent me his public key.

```bash
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCm5nNGBGmwYdGcDEQ60laushTrOAKCM3lKAI1FAKUDgatWoffzRnmFxsfoFq2MIl87YvTVLTf8ijlwKNEJdl/p9oJcPXeocKYPiFScAeTJBSEhwDy4VK1UsQytXTSzQyNxttJJAPCEzOq64CDNHb9OTspfgnFKT1gR6jONTiitdQIDAQAB
```

![my peers public key](/03_Security/images/03_assymmetric-encryption2-1.png)<br><br> 

- Step 2: I typed a message for my peer and together with his public key I encrypted this message.

```bash
e7OciQNgvqsT8vBf6tENUPLCtRK9zbM169QQRChuKQdipMv3UrriINscNz66tWKPlBhmmW6euFD4aXl4+WnT92FKR4jH7PhTHDZXyvWFgCC7F83IeR3VnF51OSOgrxmJCj15a0DCL+8pkpcz7PE9XpZZNb4JQkaxdHUvjw1RaDM=
```

![encrypted message](/03_Security/images/03_assymmetric-encryption2-2.png)<br><br>

- Step 3: This encrypted message I sent back to my peer via Slack.

![encrypted message](/03_Security/images/03_assymmetric-encryption2-3.png)<br><br>

- Step 4: He was able to decrypt the encrypted message using his private key.

- Step 5: Success!