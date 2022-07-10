Step 1: Analyze the image given to us i.e. 'hexhuebad', it is an an very famous Symbol Cipher.

![Screenshot 2022-07-11 000017](https://user-images.githubusercontent.com/90497253/178157499-5e5b072f-4d45-421e-b5b7-c0cd61843f61.png)

Can be viewed on the dcode <https://www.dcode.fr/symbols-ciphers>, you can bookmark this link (highly used in various Cryptography challenges in CTFs).

Step 2: But the issue is that the image is very big and decoding the same manually will not be feasibale. On trying the decoding some initial words we will get something like "IPSUM ....".

Based upon the same we can infer that most of the text is useless. Scroling through the image manually, in someway middle we can see a big word (which possibly could be the flag).

Step 3: Decoding the same word manually we will get 'THE_MESSAGE_YOU_SEEK_IS_IHATEHEXAHUESOMUCHPLEASEHELP' meaning flag is 'vsctf{IHATEHEXAHUESOMUCHPLEASEHELP}'.

Step 4: We can also decode the whole image using a simple Python Script provided as hexhuebad.py.
## vsctf{IHATEHEXAHUESOMUCHPLEASEHELP}
