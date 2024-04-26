
# One-time-pad Cryptography Project

## by ilGiacoo88

This is a model of how the ***one-time-pad Cryptography*** model works, written entirely in Python.

***Before starting:***
*This Cryptography method is weak and I recommend you to don't use this Cryptography project in real-world Projects, because it can be exploited in a really easy way. <br>
***So the developer assumes no responsability about this project, the way that it's used and the problems of security correleted to the project. <br>
Also this project is only for educational purposes!!***

First of all you need to open the *Encryption.py* file, then run it and insert the text that you want to encrypt.
Then the uoutput will be a secret_key and a cipher_text, remember and write them somewhere because you will need them for decryption.

Then open the *Decryption.py*, the first thing to insert is the cipher_text of before and then the secret_key.
After that the decrypted_text will be shown on the screen.

The basic foundamental of the **one-time-pad Chryptography**:
We need a Message (*m*) and a Key (*k*) to make the Cipher Text (*c*).
The algorithm used is:
~~~
c = m ^ k
~~~
and to decrypt is:
~~~
m = c ^ k
~~~

The *^* operator is the **bit-wise exclusive-OR**, its property:
~~~
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 0 = 0
~~~
If you want to learn more about this algorithm search on the Internet
<br>
<br>
Have fun and learn as much as you can from this project. <br><br>
Thank you <br>
*ilGiacoo88* <br><br><br>

***History:***<br>
1) 26/04/2024 --> Uploaded the project: ***oneTimePad_Cryptography*** with the two *python files* (*Encryption.py, Decryptio.py*), the *README.md* and the *MIT License*
