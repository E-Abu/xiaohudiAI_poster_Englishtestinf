
def save(yesterday_title):
    with open('yesterday_title_is_here' , 'w', encoding='utf-8') as f:
        f.write(yesterday_title)

def look_yesterday_title():
    with open('yesterday_title_is_here' , 'r', encoding='utf-8') as f:
        return f.read()

#save("aljflsaldfkjkahjgd;aklfd\nsafsagsdfgasf")
#print(look_yesterday_title())