
# Write a program antihtml.py that takes a URL as argument, 
# downloads the html from web and print it after stripping html tags
def antihtml(url):
    import re
    f = open(url,'r')
    pattern = re.compile(r'<\S+(\s.*?)(>)') 
    for line in f.readlines():
        match = pattern.search(line)
        if match:
            print(match.group(1))
#antihtml('index.html')

# Write a function make_slug that takes a name converts it into a slug. 
# A slug is a string where spaces and special characters are replaced 
# by a hyphen, typically used to create blog post URL from post title. 
# It should also make sure there are no more than one hyphen in any 
# place and there are no hyphens at the biginning and end of the slug.
def make_slug(text):
    import string
    text = text.strip(string.punctuation+string.whitespace)
    text_list = text.split()
    new_list = []
    for word in text_list:
        word = word.strip(string.punctuation+string.whitespace)
        new_list.append(word)
    return '-'.join(new_list)
#print(make_slug('--hello- world!--'))

def make_slug_re(text):
    import re
    matches = re.findall(r'.*?(\w+).*?',text)
    text_list=[]
    if matches:
        for match in matches:
            text_list.append(match)
    return '-'.join(text_list)
print(make_slug_re('--hello--world!-- fahim'))

