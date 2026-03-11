import json

def main():
    json_obj = [1, 2, 3, {"a": 1, "b": "Carter"}, "Emma", [True, "George"]]
    json_str = json.dumps(json_obj)

    print(json_obj)
    print(json_str)

    # How can I get "Carter" from json_obj
    print(json_obj[0]) # 1
    print(json_obj[1]) # 2
    print(json_obj[2]) # 3
    print(json_obj[3]["a"])
    print(json_obj[3]["b"]) # {"a": 1, "b": "Carter"}
    

    # How can I get "Emma" from json_obj
    print(json_obj[4]) # Emma
 

    # How can I get "George" from json_obj
    print(json_obj[5][1]) # [True, "George"]


    # Play with json_str
    print(json_str[0]) # [
    print(json_str[1]) # 1
    print(json_str[2]) # ,

    # Question: Which one is easier to take out meaningful piece of info? json_obj or json_str?
    # Answer: json_obj

    # Question: When sending a message, are we sending the json_str or json_obj?
    # Passing message to another one.
   

if __name__ == "__main__":
    main()