import json



def read_config_data() :
    
    try :
        file = open("data.json", "r")
        file.close()

    except FileNotFoundError :
        
        file = open("data.json", "w")
        json.dump({"PASSWORD" : "", "SENDER" : "", "DEST" : ""}, file)
        file.close()


    finally :
       
        file = open("data.json", "r")
        data = json.load(file)
        file.close()
        return data
    
    
read_config_data() 