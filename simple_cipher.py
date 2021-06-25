#!/usr/bin/env python3
import sys
def decryptor(message):
    message_d=""
    for character in message:
        split_message=character.split(". ")
        for items in split_message:
            the_words=items.split(" ")
            if message_d !="":
                message_d+=" "+the_words[0]
            else:
                message_d+= the_words[0]
    print(message_d)

def main():
    cypher_text=open(sys.argv[1],"r")
    decryptor(cypher_text)
    cypher_text.close()

if __name__=="__main__":
    main()
