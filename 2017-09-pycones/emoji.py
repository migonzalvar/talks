import unicodedata
s = "🤴🏻🤴🏽🤴🏿"
for c in s:
    print(unicodedata.name(c))
