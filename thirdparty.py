import requests

TOKEN_URI = "http://localhost:8000/token/"

PRODUCT_BASE_URI = "http://127.0.0.1:8000/api/product/"
CATEGORY_BASE_URI = "http://127.0.0.1:8000/api/Category/"
MOSTVIEWED_BASE_URI = "http://127.0.0.1:8000/api/mostviewed/"


# {'Authorization' : 'Token 5eb1fb18e5bfb494d8b2e502e31a03ea78ad4ca7'}
# headers = Token 5eb1fb18e5bfb494d8b2e502e31a03ea78ad4ca7
#"product": "http://127.0.0.1:8000/api/product/",
#"Category": "http://127.0.0.1:8000/api/Category/",
#"mostviewed": "http://127.0.0.1:8000/api/mostviewed/"

APP_TOKEN_SUPERUSER_GANESH = 'Token 5eb1fb18e5bfb494d8b2e502e31a03ea78ad4ca7'

dict_token_val1 = {'Authorization' : APP_TOKEN_SUPERUSER_GANESH}



def get_token_for_user(user,pwd):
    response = requests.post(TOKEN_URI,json={"username":user,"password":pwd})
    #response = requests.post(TOKEN_URI,user,pwd)
    print(response.status_code)
    print(response.json())
    return response.json()



def get_all_products(token):
    response = requests.get(PRODUCT_BASE_URI,headers = token) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())

def get_all_Category(token):
    response = requests.get(CATEGORY_BASE_URI,headers = token) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())

def get_all_mostviewed(token):
    response = requests.get(MOSTVIEWED_BASE_URI,headers = token) #guest token    --> should not be accessed
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':

    #get_token_for_user("ganesh007","ganesh007")


    print('___________________________________________________________________________')


    get_all_products(dict_token_val1)

    get_all_Category(dict_token_val1)

    get_all_mostviewed(dict_token_val1)
