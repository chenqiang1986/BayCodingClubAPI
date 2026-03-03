import base64
import requests

def main():
     

    with open('aaa.png', 'rb') as f:
        image_bytes = f.read()
        image_b64 = base64.b64encode(image_bytes).decode('utf-8')
        bytes = base64.b64decode(image_b64)

    print(image_bytes)
    print(image_b64)
    print(bytes)

    #print(f"data:image/png;base64,{image_b64}")


if __name__ == "__main__":    
    main()