#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd

for name in dir(hd):
    if name[:2] != "__":
        print(name)
