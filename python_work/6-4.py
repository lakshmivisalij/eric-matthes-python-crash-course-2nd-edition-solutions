glossary = {'print': 'prints the output', 'get': 'gets the value in the key-value pair- if value is not present, it gives the 2nd argument', 
'title': 'converts a string to title case', 'strip': 'strips the empty spaces', 'slice': 'slicing a list', 'set': 'set of elements',
'dictionary': 'key-value pairs', 'loops': 'for, while', 'list': 'a collection of items in a particular order', 'string':'a series of characters', 'boolean expression': 
'An expression that evaluates to True or False'}

for term in glossary:
	print(f"{term.title()}: {glossary[term].title()}")