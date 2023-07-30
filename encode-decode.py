import base64
import time

# Make sure your compiler can import base64 and time modules.

# Code uses utf-8 characters

def encode_string(input_string):
   # Convert string to bytes
    input_bytes = input_string.encode('utf-8')
    # Encode bytes using base64
    encoded_bytes = base64.b64encode(input_bytes)
    # Convert encoded bytes to string
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def decode_string(encoded_string):
    # Convert string to bytes
    encoded_bytes = encoded_string.encode('utf-8')
    # Decode bytes using base64
    decoded_bytes = base64.b64decode(encoded_bytes)
    # Convert decoded bytes to string
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

# User input
choice = input("Enter 'encode' to encode a string, 'decode' to decode a string: ")

if choice.lower() == 'encode':
    input_string = input("Enter a string to encode: ")
    encoded_string = encode_string(input_string)
    print("Encoded String:", encoded_string)
    print(f"\n Copy it, and run it with the decode: {encoded_string}")
    time.sleep(10)
    input("Press enter to exit. ")
    quit()
elif choice.lower() == 'decode':
    encoded_string = input("Enter a string to decode: ")
    decoded_string = decode_string(encoded_string)
    print("Decoded String:", decoded_string)
    input("Press enter to exit. ")
    quit()
else:
    print("Invalid choice. Please enter 'encode' or 'decode'.")
    input("Press enter to exit. ")
    quit()
