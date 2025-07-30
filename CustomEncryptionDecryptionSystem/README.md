# Custom Multi-layer Encryption-Decryption System

##  Description:-

This project implements a **custom, three-layer encryption and decryption system** without using any external libraries.
The layers are designed to simulate modern cryptographic pipelines by combining classical techniques with basic transformations.

## Layers Overview:-

1. **Caesar Cipher Shift**:
   - Each alphabetical character is shifted by a specified number of positions.

2. **String Reversal**:
   - The entire string is reversed after Caesar encryption to scramble the order.

3. **ASCII Shift using a Secret Key**: 
   - Every character (including special symbols and spaces) has its ASCII value increased by a secret numeric key.

The decryption process reverses the steps in the opposite order.

