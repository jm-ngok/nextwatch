import paramiko
import argparse
import difflib

from nextwatch.classes.device import Device
from prechecks import PRECHECKS
from postchecks import POSTCHECKS

# Define methods for PreChecks, PostChecks, and Compare
def run_ssh_commands(device_ip, device_admin, device_admin_password, commands, output_file, cmd_group=''):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device_ip, username=device_admin, password=device_admin_password)

        # Execute commands and write output to file
        with open(output_file, 'a') as out_file:
            out_file.write(f"[{device_ip}] [{device_admin}] [{cmd_group}]\n")
            for command in commands:
                stdin, stdout, stderr = ssh.exec_command(command)
                output = stdout.read().decode()
                out_file.write(f"Command: {command}\n")
                out_file.write(f"Output:\n{output}\n")
                out_file.write("="*50 + "\n")

        ssh.close()
        print(f"Output has been saved to {output_file}")
    except Exception as e:
        print(f"Error while SSH-ing into the device: {e}")

def compare_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            f1_lines = f1.readlines()
            f2_lines = f2.readlines()

        # Compare the two files
        diff = difflib.unified_diff(f1_lines, f2_lines, fromfile=file1, tofile=file2)

        with open(output_file, 'w') as out_file:
            for line in diff:
                out_file.write(line)

        print(f"Comparison complete. Differences saved to {output_file}")
    except Exception as e:
        print(f"Error while comparing files: {e}")

def handle_pre_post_checks(method, device, device_ip, device_admin, device_admin_password):
    # Define a set of commands based on the device and method
    output_file = f"{method}_{device}_{device_ip}.txt"
    if method == 'PreChecks':
        commands = PRECHECKS.get(device)
        for key, value in commands.items():
            run_ssh_commands(device_ip, device_admin, device_admin_password, value, output_file, key)
    elif method == 'PostChecks':
        commands = POSTCHECKS.get(device)
        for key, value in commands.items():
            run_ssh_commands(device_ip, device_admin, device_admin_password, value, output_file, key)

    if not commands:
        print(f"Unsupported device: {device}")
        return

    # Call the SSH function to run commands
    output_file = f"{method}_{device}_{device_ip}.txt"
    run_ssh_commands(device_ip, device_admin, device_admin_password, commands, output_file)

def main():
    parser = argparse.ArgumentParser(description="NextWatch: PreChecks, PostChecks, Compare")
    parser.add_argument("method", choices=["PreChecks", "PostChecks", "Compare"], help="Method to run")
    parser.add_argument("device", choices=["Router", "Switch", "Wireless Controller"], help="Device type")
    parser.add_argument("device_ip", help="IP address of the device")
    parser.add_argument("device_admin", help="Admin username for the device")
    parser.add_argument("device_admin_password", help="Admin password for the device")
    parser.add_argument("file2", nargs="?", help="Second file for comparison (only for Compare method)")

    args = parser.parse_args()

    if args.method == "Compare":
        if not args.file2:
            print("Error: Compare method requires two files to compare.")
            return
        output_file = f"compare_output_{args.device}.txt"
        compare_files(args.device_ip, args.file2, output_file)
    else:
        # device = Device(args.device, args.device_ip, args.device_admin, args.device_admin_password)
        # device.ssh_connect()
        # device.initialize_pre_checks() if args.method == "PreChecks" else device.initialize_post_checks()
        # output = device.execute_pre_checks() if args.method == "PreChecks" else device.execute_post_checks()
        # file = f"{args.method}_{args.device}_{args.device_ip}.txt"
        # device.ssh_disconnect()
        #
        # with open(file, 'w') as f:
        #     f.write("\n".join(output))

        handle_pre_post_checks(args.method, args.device, args.device_ip, args.device_admin, args.device_admin_password)

if __name__ == "__main__":
    main()
