def log_cmd(command):
    try:
        # Open the file in write mode ('w') or append mode ('a')
        with open('logged_chats\logs.txt', 'w') as file:
            # Write the specified text to the file
            file.write(command)
    except Exception as e:
        print(f"An error occurred: {e}")