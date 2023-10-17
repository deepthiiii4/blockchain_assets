# blockchain in Land Ownership Tracking Blockchain

This is a simple Python-based blockchain prototype designed to track land ownership details using a blockchain structure. It allows users to add, modify, view, and remove blocks containing land ownership information.

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Blockchain Structure](#blockchain-structure)
- [File Management](#file-management)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the script using `python blockchain.py`.

## Usage

1. **Add a New Block**: Choose option 1 to add a new block to the blockchain. You will be prompted to input land ownership details such as owner name, patta number, land latitude, geo-location, and address.

2. **View the Blockchain**: Select option 2 to view the entire blockchain. It displays the index, timestamp, and data for each block, including land ownership details.

3. **Save the Blockchain to a File**: Choose option 3 to save the blockchain to a text file named 'blockchain.txt'.

4. **Modify Land Details**: Select option 4 to modify land ownership details within a specific block. You will be prompted to enter the patta number of the block you want to modify. Then, you can choose which details to update.

5. **Remove a Block**: Option 5 allows you to remove a specific block by entering its index. The block will be permanently removed from the blockchain, and the text file will be updated accordingly.

6. **Exit**: To exit the program, choose option 6.

## Features

- Blockchain structure with the ability to add, view, modify, and remove blocks.
- Data integrity ensured through hash calculations.
- Loading and saving the blockchain to a text file.
- Basic user interface for interacting with the blockchain.

## Blockchain Structure

The blockchain consists of blocks, each containing the following information:

- Index: A unique identifier for the block.
- Previous Hash: The hash of the previous block, ensuring data integrity.
- Timestamp: The time at which the block was created.
- Data: Land ownership details, including owner name, patta number, land latitude, geo-location, and address.
- Hash: The hash of the block's data for verification.

## File Management

The blockchain data is stored in a text file named 'blockchain.txt.' The script reads and writes data to this file to maintain the state of the blockchain.

## Contributing

Contributions to enhance and expand this project are welcome. If you have ideas or improvements to suggest, feel free to create a pull request.


