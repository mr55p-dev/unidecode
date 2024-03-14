import sys
import json 

def main():
    with open("symbolsMap.json", "r") as f:
        symbolsMap = f.read()
    symbolsMap = json.loads(symbolsMap)
    inp = sys.argv[1].replace(" ", "").lower()
    buf = []
    i = 0
    print(f"|Char  | Symbol   | Description")
    while i < len(inp):
        buf.append(inp[i])
        candSymbol = "".join(buf)
        if candSymbol not in symbolsMap:
            if len(buf) > 8:
                raise ValueError(f"Invalid buffer {candSymbol}")
            i += 1
            continue

        char = bytes.fromhex(candSymbol).decode("utf-8")
        print(f"| {char:4} | {candSymbol:8} | {symbolsMap[candSymbol]}")
        buf.clear()
        i += 1



main()
