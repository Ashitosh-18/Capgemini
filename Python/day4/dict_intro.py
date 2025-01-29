dict1={}
print("It is an empty dictionary")

dict2={'eggs':3,'fruits':4}
print("items in dict are:",dict2['eggs'])

dict3={'food':{'eggs':3,'fruits':4}}
print("items in dict are:",dict3['food'])

dict4=dict(name='Ash',age=20)
print("items in dict are:",dict4)

keyslist=[1,2,3]
valslist=['mango','apple','grapes']
dict5=dict(zip(keyslist,valslist))
print("items in dict are:",dict5)

dict6={'eggs':3,'fruits':4,'beer':2,'cake':8}

print(dict6.keys())

print(dict6.values())

print(dict6.items())

print(dict6.copy())

print(dict6.get('beer'))

print(dict6.update(dict4))

print(dict6.pop('beer'))

print(len(dict6))


