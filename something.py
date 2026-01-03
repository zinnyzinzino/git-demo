from datetime import datetime

x = datetime.now()

filename = x.strftime("%d-%m-%Y.txt")
with open(filename, "w") as fp:
    print("created", filename)
    fp.write("hello")

fn = open(filename, "r")
print(fn.read())
fn.close
