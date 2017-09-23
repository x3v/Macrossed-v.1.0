import safygiphy
g = safygiphy.Giphy()
r = g.random(tag="macross")
# Will return a random GIF with the tag "success"
print(r['data']['url'])
