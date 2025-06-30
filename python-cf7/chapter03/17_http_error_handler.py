def get_http_error(error_code):
    error_messages = {200: "OK", 400: "Bad request", 404: "Not found"}
    return error_messages.get(error_code, "Unkown Error")
    
    

def main():
    error_code = 404
    print(get_http_error(error_code))


if __name__ == "__main__":
    main()