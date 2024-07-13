import imaplib, email

def reciever_check(imap_server, reciever_email, reciever_pass):
    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(reciever_email, reciever_pass)
        print("Login successful\n")
        return imap
    except:
        print("Error, invalid credentials\n")

def reciever_read(imap, reciever_number):
    _, msgnums = imap.search(None, "ALL")
    valid_pnum = {}
    for msg in msgnums[0].split():
        _, data = imap.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        strmsg = []
        strmsg.append(message.get("From"))
        strmsg.append("")
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                strmsg[1] += part.as_string()
        strmsg[0] = filter_message(strmsg[0], "<", ">")
        if(strmsg[0][:11] == reciever_number):
            strmsg[1] = filter_message(strmsg[1], "<https://voice.google.com>", "YOUR ACCOUNT")
            if strmsg[1].count("\n"):
                strmsg[1] = strmsg[1][:strmsg[1].index("\n")]
            valid_pnum[strmsg[0][12:23]] = strmsg[1]
    return valid_pnum

def filter_message(msg, start_condition, end_condition):
    start_index = msg.find(start_condition) + len(start_condition)
    end_index = msg.find(end_condition)
    content = msg[start_index:end_index].strip()
    return content