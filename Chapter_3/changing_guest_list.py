guest_list = ['saiki', 'saiko', 'kusuke']
message = "you are invited to a meal at my place."

print(f"Dear {guest_list[0].title()}, {message}")
print(f"Dear {guest_list[1].title()}, {message}")
print(f"Dear {guest_list[2].title()}, {message}")

print(f"\n{guest_list[1].title()} has denied to attend the meal. Reasoning: lower class meal.")
del guest_list[1]

guest_list.append('teruhashi')

print(f"\nDear {guest_list[0].title()}, {message}")
print(f"Dear {guest_list[1].title()}, {message}")
print(f"Dear {guest_list[2].title()}, {message}")

print("\nHello everyone, I have found more space and a bigger table for the dinner")

guest_list.insert(0, 'nendo')
guest_list.insert(1, 'kaido')
guest_list.append('hairo')

print(f"Dear {guest_list[0].title()}, {message}")
print(f"Dear {guest_list[1].title()}, {message}")
print(f"Dear {guest_list[2].title()}, {message}")
print(f"Dear {guest_list[3].title()}, {message}")
print(f"Dear {guest_list[4].title()}, {message}")
print(f"Dear {guest_list[5].title()}, {message}")

print("\nSorry everyone it seems I can only invite two people.")

removed_guest = guest_list.pop()
print(f"\nI am extremely sorry {removed_guest.title()} for being unable to host you for dinner.")

removed_guest = guest_list.pop()
print(f"\nI am extremely sorry {removed_guest.title()} for being unable to host you for dinner.")

removed_guest = guest_list.pop()
print(f"\nI am extremely sorry {removed_guest.title()} for being unable to host you for dinner.")

removed_guest = guest_list.pop()
print(f"\nI am extremely sorry {removed_guest.title()} for being unable to host you for dinner.")

print(f"\nDear {guest_list[0].title()}, {message}")
print(f"Dear {guest_list[1].title()}, {message}")

print(len(guest_list))

del guest_list[0]
del guest_list[0]
print(guest_list)