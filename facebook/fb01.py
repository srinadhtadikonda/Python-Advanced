import json 
import facebook 
  
def main(): 
    token = "Please replace this line with your access token"
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields ='first_name, gender, birthday, email')  
     
    # return desired fields 
    print(json.dumps(profile, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
