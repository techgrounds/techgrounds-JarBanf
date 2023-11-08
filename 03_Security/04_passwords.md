# Passwords
A password is a secret word or phrase or code that you need to know in order to have access to a place or system. In technical terms, it is a series of letters or numbers that you must type into a computer or computer system in order to be able to use it.  
Passwords are our first line of defense. In a manner of speaking, we are only as strong as our weakest password.


## Key-terms


## Assignment
1. Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
2. Find out how a Rainbow Table can be used to crack hashed passwords.
3. Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
```
03F6D7D1D9AAE7160C05F71CE485AD31
```
```
03D086C9B98F90D628F2D1BD84CFA6CA
```
4. Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
5. Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.

### Used sources
- [Password Management in Cyber Security](https://www.geeksforgeeks.org/password-management-in-cyber-security/)
- [What’s in a Strong Password?](https://www.csum.edu/it/media/what-is-in-a-good-password.pdf)
- [What Is Hashing, and How Does It Work?](https://www.codecademy.com/resources/blog/what-is-hashing/)
- [Safely Storing User Passwords: Hashing vs. Encrypting](https://www.darkreading.com/risk/safely-storing-user-passwords-hashing-vs-encrypting)
- [Hashing vs. encryption: What’s the difference?](https://nordvpn.com/blog/hashing-vs-encryption/)
- [Understanding Rainbow Table Attack](https://www.geeksforgeeks.org/understanding-rainbow-table-attack/)
- [MD5 Center](https://md5.gromweb.com/)
- [Understanding /etc/shadow file format on Linux](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)
- [Free Password Hash Cracker](https://crackstation.net/)

### Encountered problems
None

### Result
**1. Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.**

Hashing is the process of converting data (text, numbers, files, or anything) into a fixed-length string of letters and numbers. Data is converted into these fixed-length strings, or hash values, by using a special algorithm called a hash function. 

For example, a hash function that creates 32-character hash values will always turn text input into a unique 32-character code. Whether you want to generate a hash value for the word "Techgrounds" or for the entire works of Shakespeare, the hash value will always be 32 characters long.

Hashing is a one-way process that can't be directly reversed to obtain the original input value (for example username and passwords).  
Symmetric encryption is based on the use of an encryption key and is a reversible operation. Anyone possesing the key can decrypt an encrypted value to obtain the original value. 

When companies store user data (for example username and passwords), they can apply hashing algorithms to ensure that the information stays private, even if they suffer a data breech.

**2. Find out how a Rainbow Table can be used to crack hashed passwords.**

The passwords in a computer system are not stored directly as plain texts but are hashed using encryption. Whenever a user enters a password, it is converted into a hash value and is compared with the already stored hash value. If the value match, the user is authenticated.

A rainbow table is a database that is used to gain authentication by cracking the password hash. It is a precomputed dictionary of plaintext passwords and their corresponding hash values that can be used to find out what plaintext password produces a particular hash. Since more than one text can produce the same hash, it's not important to know what the original password really was, as long as it produces the same hash.

**3. Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.**

- Using MD5 reverse lookup the MD5 hash `03F6D7D1D9AAE7160C05F71CE485AD31` was succesfully reversed into the string `welldone!`.

![md5 reverse lookup](/03_Security/images/04_passwords3-1.png)<br><br>

- Using MD5 reverse lookup the MD5 hash `03D086C9B98F90D628F2D1BD84CFA6CA` could not be reversed into a string: no reverse string was found.

![md5 reverse lookup](/03_Security/images/04_passwords3-2.png)<br><br>

**4. Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.**

- Created test_pass_user:
```
sudo useradd test_pass_user
```
- Created password for test_pass_user. Password is `12345`.:
```
sudo passwd test_pass_user
```
- The hash for password `12345` is:  
`$6$em/RM4xaNeTtQYn5$mk3gEZ.pBx00CDywbmODTId010adKdUPwXi5/Xz/aQWw9Dp.WHM05k3g7rnGE6eXTLlrC3IfqCFJBI3Db3UCe0`

![hash](/03_Security/images/04_passwords4-1.png)<br><br>

- The `$6` at the beginning of the hash is the algorithm prefix used for this password. In this case, it is a SHA-512 hash (512 bits). SHA stands for Secure Hash Algorithm. Using Free password hash cracker I can't crack the hash because the hash is salted.

![hash lookup](/03_Security/images/04_passwords4-2.png)<br><br>

**5. Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.**

Salting a piece of data is done by adding additional random characters to the text in order to strengthen it. This is mostly done with passwords: adding random characters to the beginning or end of a password to prevent it from being easily guessed by a hacker.

![salted hash comparison from same password 12345](/03_Security/images/04_passwords5.png)<br><br>