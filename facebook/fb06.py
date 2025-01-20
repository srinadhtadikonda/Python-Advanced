import json 
import facebook 
  
def main(): 
    token = "Please replace with your access token"
    graph = facebook.GraphAPI(token) 
  
    places = graph.search(type ='place', center ='28.6304, 77.2177',  
                                            fields ='name, location') 
  
    for place in places['data']: 
        print('%s %s' %(place['name'].encode(), place['location'].get('zip'))) 
      
if __name__ == '__main__': 
    main() 
