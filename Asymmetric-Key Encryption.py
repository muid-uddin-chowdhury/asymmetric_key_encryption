import rsa

# generates public and prrivate keys with
# rsa.newkeys method, this method accepts
# 1. background studies on the paper "Bumblebee" I presented in the last meeting. 2. Learning new encryption method such as AES256 and RSA. 3. Understading the differences between assymetric ans symmetric encruption methods. 4. Check the paper Nimbus the weakness of SIp and do the mathematical representations to check each of the weakness whetaher they are correct or not. 5. Implement COP in python. 6 try to understand COP 
# key lenght as it's parameters 
# key lenght should be at least 16
publicKey, privateKey = rsa.newkeys(512)

# that is the key that will be encrypted 
message = "hello geeks"

# rsa.encrypt is used to encrypt 
# string with public key string should be 
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(), publicKey)

print("Original String:", message)
print("Encrypted String:", encMessage)

# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte strings 
# use decode method to convert it to string 
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("Decrypted String:", decMessage)