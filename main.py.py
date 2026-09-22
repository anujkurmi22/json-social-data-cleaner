import json
def load_data(file_name):
    with open(file_name,"r")as file:
        data = json.load(file)
    return data

data = load_data("anuj1.json")

def display_data(data):
    print("*______________USER____________*")
    for user in data["users"]:
       
        print(f"User id: {user['id']}\t Friends :{user['friends']}\tLike pages: {user['liked_pages']}")
    print("*______________PAGE____________*")
    for page in data["pages"]:
        
        print(f"Page id: {page['id']}\t Page name: {page['name']}")

display_data(data)

# clean dubble data 
def cleaned_data(data):
    #remove user with missing name 
    data["users"] = [user for user in data ['users'] if user["name"].strip()]
    # remove duplicate friends
    for user in data ["users"]:
        user["friends"] = list(set(user["friends"]))

    #remove inactive user 
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

    #remove duplicate pages
    unique_pages = {}
    for page in  data ["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())
    return data 

data = json.load(open("anuj2.json"))
prepared_data = cleaned_data(data)
json.dump(prepared_data,open("cleaned_data.json","w"),indent=4)
print("data clean successfully")