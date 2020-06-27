
harrison = {}
harrison['name'] = "Christopher"
harrison['surname'] = "Harrison"

susan = {}
susan['name'] = "Susan"
susan['surname'] = "Ibach"

people = []
people.append(harrison)
people.append(susan)
people.append({
    'name': 'Bill', 'surname':'Gates'
})

print(people)
