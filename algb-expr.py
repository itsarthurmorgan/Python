AlgExpr = input("Enter algebric expression: ")
ConvertedExpr = ''
for ch in AlgExpr:
    if ch>='0' and ch<='9':
        ConvertedExpr = ConvertedExpr + ch
    elif ch=='(':
        ConvertedExpr = ConvertedExpr + '*' + ch
    elif ch>='a' and ch<='z' and ConvertedExpr[-1]!='(':
        ConvertedExpr = ConvertedExpr + '*' + ch
    else:
        ConvertedExpr = ConvertedExpr + ch
print("Converted expression is :",ConvertedExpr)