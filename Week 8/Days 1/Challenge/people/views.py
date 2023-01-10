from django.shortcuts import render


# Create your views here.
def people(request):

    people = [
        {
            'id': 1,
            'name': 'Bob Smith',
            'age': 35,
            'country': 'USA'
        },
        {
            'id': 2,
            'name': 'Martha Smith',
            'age': 60,
            'country': 'USA'
        },
        {
            'id': 3,
            'name': 'Fabio Alberto',
            'age': 18,
            'country': 'Italy'
        },
        {
            'id': 4,
            'name': 'Dietrich Stein',
            'age': 85,
            'country': 'Germany'
        }
    ]

    trie = sorted(people, key=lambda d: d['age'])
    context = {
        "people": trie,
    }
    return render(request, "people/page.html", context)

def people_one(request, id):
    people2 = []
    for i in people:
        if i['id'] == id:
            people2.append(i)
    context = {
        "data": people2
    }
    return render(request, "people/person.html", context)