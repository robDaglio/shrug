#!/usr/bin/env python
import pyperclip

SHRUG = '¯\_(ツ)_/¯'

if __name__ == '__main__':
    try:
        pyperclip.copy(SHRUG)
        print(f'{SHRUG} | Copied to clipboard.')
    except Exception as e:
        print('Something went wrong >.<')
 
