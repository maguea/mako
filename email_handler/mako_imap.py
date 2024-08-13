import imaplib, email, re
    
# Check login credentials
def reciever_check(reciever_imap_server, reciever_email, reciever_pass):
    try:
        # Connect and login to server
        imap = imaplib.IMAP4_SSL(reciever_imap_server)
        imap.login(reciever_email, reciever_pass)
        print("IMAP login successful")
        return imap
    except:
        print("Error, invalid credentials\n") #Program will end without proper credentials

# Read all emails, return dictionary => {'sender address' : 'message'}
def reciever_read(imap, reciever_number):
    # Determine search range
    _, msgnums = imap.search(None, "ALL") 
    valid_pnum = {}

    for msg in msgnums[0].split():
        # Decode and store messages
        _, data = imap.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        strmsg = []
        strmsg.append(message.get("From"))
        strmsg.append("")
        # Store text from messages
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                strmsg[1] += part.as_string()
        # Extract the address
        strmsg[0] = filter_message(strmsg[0], "<", ">")
        # Check msg validity
        if(strmsg[0][:11] == reciever_number):
            strmsg[1] = filter_message(strmsg[1], "<https://voice.google.com>", "YOUR ACCOUNT")
            # Truncate digital signature
            if strmsg[1].count("\n"):
                strmsg[1] = strmsg[1][:strmsg[1].index("\n")]
            # Store filtered data
            valid_pnum[strmsg[0]] = strmsg[1]
        # Delete original email
        imap.store(msg, '+FLAGS', '\\Deleted')

    return valid_pnum

# Extract data from given range => 'start' 'return text' 'end'
def filter_message(msg, start_condition, end_condition):
    # Set boundaries
    start_index = msg.find(start_condition) + len(start_condition)
    end_index = msg.find(end_condition)
    # Remove text outside of range
    content = msg[start_index:end_index].strip()

    return content

# Finds largest integer in text => 'hght &7 88' gets '88'
def get_msg_count(msg):

    pattern = r'\b\d+\b'  # \b matches word boundaries, \d+ matches one or more digits
    integers = re.findall(pattern, msg)

    if not integers:
        return 0
    else:
        return int(max(integers))