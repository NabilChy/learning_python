def send_messages(messages, sent_messages):
    '''Moves the messages to sent_messages and prints the original list'''
    while messages:
        current_message = messages.pop()
        print(f"Printing messages: {current_message}")
        sent_messages.append(current_message)
    

def show_messages(sent_messages):
    '''Prints the messages in a list '''
    for message in sent_messages:
        print(f"\n{message}")

messages =['Hello', 'Good Day to You']
sent_messages =[]

send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print(messages)
print(sent_messages)