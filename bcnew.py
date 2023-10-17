import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def calculate_hash(self):
        value = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", "0")

def create_new_block(previous_block):
    index = previous_block.index + 1
    timestamp = int(time.time())
    owner_name = input(f"Enter the name of the land owner for Block #{index}: ")
    patta_number = input(f"Enter the patta number for Block #{index}: ")
    land_latitude = input(f"Enter the land latitude for Block #{index}: ")
    geo_location = input(f"Enter the geo-location for Block #{index}: ")
    address = input(f"Enter the address for Block #{index}: ")
    data = {
        "Owner Name": owner_name,
        "Patta Number": patta_number,
        "Land Latitude": land_latitude,
        "Geo Location": geo_location,
        "Address": address
    }
    hash = previous_block.calculate_hash()
    return Block(index, previous_block.hash, timestamp, data, hash)

def modify_block_details(blockchain):
    patta_number = input("Enter the patta number of the block you want to modify: ")
    for block in blockchain:
        if "Patta Number" in block.data and block.data["Patta Number"] == patta_number:
            print(f"Modifying details for Block #{block.index} with Patta Number: {patta_number}")
            print("Options to modify:")
            print("1. Owner Name")
            print("2. Land Latitude")
            print("3. Geo Location")
            print("4. Address")
            option = input("Enter the option number to modify: ")
            if option == '1':
                owner_name = input("Enter the new owner name: ")
                block.data["Owner Name"] = owner_name
            elif option == '2':
                land_latitude = input("Enter the new land latitude: ")
                block.data["Land Latitude"] = land_latitude
            elif option == '3':
                geo_location = input("Enter the new geo location: ")
                block.data["Geo Location"] = geo_location
            elif option == '4':
                address = input("Enter the new address: ")
                block.data["Address"] = address
            else:
                print("Invalid option. No changes were made.")
            return
    print(f"Block with Patta Number {patta_number} not found in the blockchain.")

def remove_block(blockchain, filename):
    index_to_remove = int(input("Enter the index of the block to remove: "))
    for block in blockchain:
        if block.index == index_to_remove:
            blockchain.remove(block)
            print(f"Block #{index_to_remove} has been removed from the blockchain.")
            update_text_file(blockchain, filename)
            return
    print(f"Block #{index_to_remove} not found in the blockchain.")

def update_text_file(blockchain, filename):
    with open(filename, 'w') as file:
        for block in blockchain:
            file.write(f"Block #{block.index}\n")
            file.write(f"Timestamp: {block.timestamp}\n")
            file.write("Data:\n")
            for key, value in block.data.items():
                file.write(f"{key}: {value}\n")
            file.write(f"Previous Hash: {block.previous_hash}\n")
            file.write(f"Hash: {block.calculate_hash()}\n\n")

def save_blockchain_to_file(blockchain, filename):
    with open(filename, 'w') as file:
        for block in blockchain:
            file.write(f"Block #{block.index}\n")
            file.write(f"Timestamp: {block.timestamp}\n")
            file.write("Data:\n")
            for key, value in block.data.items():
                file.write(f"{key}: {value}\n")
            file.write(f"Previous Hash: {block.previous_hash}\n")
            file.write(f"Hash: {block.calculate_hash()}\n\n")

def load_blockchain_from_file(filename):
    blockchain = []
    with open(filename, 'r') as file:
        lines = file.read().split('\n\n')
        for block_data in lines:
            lines = block_data.split('\n')
            if len(lines) >= 5:
                index = int(lines[0].split('#')[1])
                timestamp = int(lines[1].split(': ')[1])
                data = {}
                for line in lines[2:-2]:
                    parts = line.split(': ', 1)  # Split only at the first occurrence of ":"
                    if len(parts) == 2:
                        key, value = parts
                        data[key] = value
                previous_hash = lines[-2].split(': ')[1]
                hash = lines[-1].split(': ')[1]
                blockchain.append(Block(index, previous_hash, timestamp, data, hash))
            else:
                print(f"Skipping invalid block data:\n{block_data}\n")

    return blockchain

filename = 'blockchain.txt'

# Check if a blockchain file exists and load it, or create a new blockchain
try:
    blockchain = load_blockchain_from_file(filename)
    print("Blockchain loaded from file.")
except FileNotFoundError:
    blockchain = [create_genesis_block()]
    print("New blockchain created.")

while True:
    print("\nOptions:")
    print("1. Add a new block")
    print("2. View the blockchain")
    print("3. Save the blockchain to a file")
    print("4. Modify Land Details")
    print("5. Remove a Block")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_block = create_new_block(blockchain[-1])
        blockchain.append(new_block)
        print(f"Block #{new_block.index} has been added to the blockchain!")

    elif choice == '2':
        for block in blockchain:
            print(f"Block #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print("Data:")
            for key, value in block.data.items():
                print(f"{key}: {value}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.calculate_hash()}\n")

    elif choice == '3':
        save_blockchain_to_file(blockchain, filename)
        print("Blockchain saved to a file.")

    elif choice == '4':
        modify_block_details(blockchain)

    elif choice == '5':
        remove_block(blockchain, filename)

    elif choice == '6':
        break
