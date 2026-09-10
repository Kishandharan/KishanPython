from cryptography.fernet import Fernet 

fernet1 = Fernet(b'JXQbeb6lr2qeNzzKylSlz_TslLCz4sTXMyLHJnCWLD8=')

f1 = open("ransom1.py", "rb+")
f1.write(fernet1.encrypt(f1.read()))
f1.close()
