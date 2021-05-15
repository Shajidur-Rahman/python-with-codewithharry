disk = {
    'name':'spacify as something ',
    'consider':'At the moment, artemisinin-based therapies are considered the best treatment, but cost about $10 per dose - far too much for impoverished communities.',
    'minute':'The minute stain on the document was not visible to the naked eye.',
    'accord':'The committee worked in accord on the bill, and it eventually passed.'
}
inp = input("Look up a word: ")
get =  disk.get(inp)
print(f"The meaning of the word {inp} is \n{get}")