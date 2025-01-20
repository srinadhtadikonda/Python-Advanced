
import json 
import facebook 
  
def main(): 
    token = "Please replace this line with your access token"
    graph = facebook.GraphAPI(token) 
    page = graph.get_object(id ='PAGEID', fields ='about, can_post, category') 
  
    # return desired fields 
    print(json.dumps(page, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
