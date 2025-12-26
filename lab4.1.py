import subprocess  # Системийн команд ажиллуулах
import os

def main():
    print("=== Mini-Batch Emulator ===")
    print("Товч: exit гээд гарах")
    
    while True:
        command = input("cmd> ")  # Хэрэглэгчээс команд унших
        
        if command.lower() == "exit":
            print("Програм дууслаа")
            break
        
        try:
            # Командыг ажиллуулах
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            # Хэрвээ алдаа гарсан бол
            if result.stderr:
                print("Алдаа:", result.stderr)
            
            # Үр дүнг хэвлэх
            if result.stdout:
                print(result.stdout)
                
        except Exception as e:
            print("Алдаа гарлаа:", e)

if __name__ == "__main__":
    main()
