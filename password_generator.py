import secrets
from pathlib import Path

print('Selamat datang di Password Generator!')

FILE_DIR = Path('secrets.key')

def menu():
    pass

def create_secrets():
    create_secrets = secrets.token_hex(8)
    
    if FILE_DIR.is_dir():
        with open(FILE_DIR, 'w') as f:
            f.write(create_secrets)
    else: 
        print('Error: File is exist')

def create_random_password(password):
    try: 
        with open(FILE_DIR, 'r') as f:
            res = f.readline()
            checking = input('Masukan secret key anda: ')
    except FileNotFoundError as e:  
        return f"Error: File Not Found\nReference: {e}"
        
    
    
    
if __name__ == "__main__":
    create_random_password('adfsafdf')
    pass    