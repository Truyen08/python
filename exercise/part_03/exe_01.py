# process try catch in open file case if file not found
filename = 'test.txt'
try:
    with open(filename) as f_obj:
         contents = f_obj.read()
except FileNotFoundError:
     msg = "--> File " + filename + "không tồn tại."
     print(msg)
