#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:21:52 2023

@author: isisbryanna
"""
import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') +
                    str(self.previous_hash).encode('utf-8') +
                    str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined:", self.hash)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(4)  # Difficulty level of 4
        self.chain.append(new_block)

class Tee:
    def getTrustedTime(self):
        return datetime.datetime.now()

    def attestation(self, nonce, l, value):
        pass

def incrementMonotonicCounter():
    global counter
    counter += 1

#First and second block 
def PoLRound(block_data1, block_data2):
    global roundBlock, roundTime, blockchain, ROUND_TIME  # Declare global variables
    
    blockchain = Blockchain()
    roundBlock = block_data1
    roundTime = tee.getTrustedTime()

    if roundTime is None:
        print("Error: getTrustedTime returned None")
        return

    # Create and mine the first block
    new_block1 = Block(roundBlock, blockchain.chain[-1].hash)
    new_block1.mine_block(4)
    blockchain.chain.append(new_block1)

    # Create and mine the second block
    roundBlock = block_data2
    new_block2 = Block(roundBlock, blockchain.chain[-1].hash)
    new_block2.mine_block(4)
    blockchain.chain.append(new_block2)

    roundBlock = None  # Reset roundBlock
    ROUND_TIME = datetime.timedelta(seconds=0)  # Reset ROUND_TIME

    return blockchain  # Return the blockchain object


def PoLMine(header_data, previous_block_data, blockchain, roundTime):
    global roundBlock, counter
    
    if roundTime is None:
        print("Error: roundTime is None")
        return

#first block I should be getting None.. as it is the first block 
#second block should be a print statment as we move forward 

    print("\nhash(previous_block_data):", hash(previous_block_data))
    assert hash(header_data) == hash(previous_block_data)

    now = tee.getTrustedTime()
    assert now >= roundTime + ROUND_TIME

    print("counter before increment:", counter)

    incrementMonotonicCounter()
    
    print("counter after increment:", counter)

    roundBlock = 1  # Set to a default value if needed
    roundTime = tee.getTrustedTime()

    l = getRandom()
    sleep(f(l))

    newCounter = readMonotonicCounter()
    print("newCounter:", newCounter)

    assert counter == newCounter

    nonce = hash(header_data)
    return tee.attestation((nonce, l), None)

def getRandom():
    pass

def sleep(t):
    pass

def f(l):
    pass

def hash(obj):
    pass

def readMonotonicCounter():
    pass

# Assuming that tee is an instance of the Tee class
tee = Tee()

# Define the value of ROUND_TIME as needed
ROUND_TIME = 0

#Change name from counter --> counter1 
#This is where im getting an error maybe we can change the name of counter to counter1
counter = 0  # Added global counter
blockchain = Blockchain()  # Added instance of Blockchain
incrementMonotonicCounter()
#PoLRound('block_data')
PoLRound('block_data1', 'block_data2')
result = PoLMine('header_data', 'previous_block_data', blockchain, roundTime)
