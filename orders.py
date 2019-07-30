# using open(), built in functionality from python to open files

try: # tries to run block of code
    file = open('order.txt','r')
    file_line_list = file.readlines()
    # print(file_line_list)
    for line in file_line_list:
        print(line.rstrip('\n'))

    file.close() # closes file, if you don't can cause a lock in the file -
except FileNotFoundError as errmsg: # if it fails it runs this block of code
    print("404")
    # print(errmsg) # captured error message
    raise # sends the default error & stops code