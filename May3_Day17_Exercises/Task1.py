users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]


def has_hits_v1(author):
    for user in users:
        if author == user['name']:
            for item in user['items']:
                if item.get('reads', 0) >= 1000:
                    return True
    return False


# alternate way


def has_hits_v2(author):
    author = [in_author for in_author in users if author == in_author['name']]
    #print(author)
    if not author:
        return False
    # alternate way
    #items = [item for item in author[0]['items'] if "items" in author[0] and item.get('reads', 0) > 1000]

    items = [item for item in author[0]['items'] if author[0]['items'] and item.get('reads', 0) > 1000]
    if items:
        return True
    return False


if __name__ == '__main__':
    print("Clark", has_hits_v1("Clark"))
    print("Peter", has_hits_v1("Peter"))
    print("Samantha", has_hits_v1("Samantha"))
    print("Mathilda", has_hits_v1("Mathilda"))
    print("Mario", has_hits_v1("Mario"))

    print("Clark", has_hits_v2("Clark"))
    print("Peter", has_hits_v2("Peter"))
    print("Samantha", has_hits_v2("Samantha"))
    print("Mathilda", has_hits_v2("Mathilda"))
    print("Mario", has_hits_v2("Mario"))
