# unidecode

Prints a description of each unicode character in a given hex dump

## Generate the symbols map from the symbol table

```!bash
jq 'map({ (."UTF-8\n(hex.)"|sub(" ";"")):(.name|tostring)}) | add' < symbols.json > symbolsMap.json
```

