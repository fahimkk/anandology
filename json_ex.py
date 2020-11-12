"""{
    "name": "Advanced Python Training",
    "date": "October 13, 2012",
    "completed": false,
    "instructor": {
        "name": "Anand Chitipothu",
        "website": "http://anandology.com/"
    },
    "participants": [
        {
            "name": "Participant 1",
            "email": "email1@example.com"
        },
        {
            "name": "Participant 2",
            "email": "email2@example.com"
        }
    ]
}"""

def escape_string(s):
    """ Escapes double-quote tab and new line
    characters in a string."""
    s = s.replace('"','\\"')
    s = s.replace('\t','\\t')
    s = s.replace('\n','\\n')
    return s

def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        return "{" + ", ".join(json_encode(k) + ':'+ json_encode(v) for k,v in data.items()) + "}"
    else:
        raise TypeError ("%s is not JSON serializable" %repr(data))

a = ['fahim',3,"ss",True]
b = {'faj':45,'sh':True,'fsh':'sh'}
print(json_encode(a))
print(json_encode(b))
print(escape_string("s'sk"))
