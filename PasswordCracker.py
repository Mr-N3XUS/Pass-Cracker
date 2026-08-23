import random
import string
import time

def smart_password_cracker():
    password = input("Enter password: ")
    

    char_sets = {
        'lower': string.ascii_lowercase if any(c.islower() for c in password) else '',
        'upper': string.ascii_uppercase if any(c.isupper() for c in password) else '',
        'digits': string.digits if any(c.isdigit() for c in password) else '',
        'punctuation': string.punctuation if any(c in string.punctuation for c in password) else ''
    }
    
    characters = ''.join(char_sets.values())
    
    if not characters:
        characters = string.ascii_letters + string.digits
    
    print(f"Analyzing password...")
    print(f"Password length: {len(password)}")
    print(f"Character set size: {len(characters)}")
    print(f"Maximum possible combinations: {len(characters) ** len(password):,}")
    print("-" * 50)
    
    guess = ""
    attempts = 0
    start_time = time.time()
    
    print("Starting brute-force attack...\n")
    
    while guess != password:
        guess = ''.join(random.choice(characters) for _ in range(len(password)))
        attempts += 1
        
        if attempts % 5000 == 0:
            elapsed = time.time() - start_time
            speed = attempts / elapsed if elapsed > 0 else 0
            print(f"Attempts: {attempts:,} | Speed: {speed:,.0f} guesses/sec | Current: {guess}", end='\r')
    
    end_time = time.time()
    
    print("\n" + "="*61)
    print(f"🎉 CRACKED! Password found: '{guess}'")
    print(f"📈 Statistics:")
    print(f"   • Total attempts: {attempts:,}")
    print(f"   • Time: {end_time - start_time:.2f} seconds")
    print(f"   • Speed: {attempts/(end_time-start_time):,.0f} guesses/second")
    print("="*20,"Developed by Mr-B1nary","="*20)

if __name__ == "__main__":

    smart_password_cracker()
