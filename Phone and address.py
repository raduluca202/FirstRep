def printList():
  for i in range(len(phones)):
    print(names[i]+ '- ' + phones[i] +'- ' + dobs[i] +'- ' + areas[i])


names = ['Stefan','Joan', 'Martin']
phones = ['01-2457738', '088-123 456', '087-3399233']
dobs = ['14/02/2002', '21/01/2001', '20/02/1999']
areas = ['Raheny', 'Baldoyle', 'Marino']
codes = ['Dublin 5', 'Dublin 13', 'Dublin 3']

printList()

names = ['Stefan','Joan', 'Martin']
phones = ['01-2457738', '088-123 456', '087-3399233']
dobs = ['14/02/2002', '21/01/2001', '20/02/1999']
areas = ['Raheny', 'Baldoyle', 'Marino']
codes = ['Dublin 5', 'Dublin 13', 'Dublin 3']



newName = input('Enter a name:')
names.append(newName)
newPhone = input('Enter a phone number:')
phones.append(newPhone)
newDobs = input('Enter a dob:')
dobs.append(newDobs)
newArea = input('Enter a area:')
areas.append(newArea)
newCode = input('Enter a code:')
codes.append(newCode)

printList()
