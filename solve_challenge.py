#! /usr/bin/python3
import base64

def solve():
    base64_bytes = secret.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')[::-1]
    print(message)

if __name__ == "__main__":
    secret = "aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K"
    solve()
