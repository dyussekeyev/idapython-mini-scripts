import ida_bytes

filename = 'C:\\Users\\User\\Desktop\\result.bin'
ea_begin = 0x001C0020

print('\n\nBegin')
with open(filename, 'rb') as input:
    bytes = input.read()
    print('Size of file = ', len(bytes))
ida_bytes.patch_bytes(ea_begin, bytes)
print('End')
