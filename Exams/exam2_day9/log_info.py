class Logger:
    def log(self,message,type):
        if type=="error":
            print(f"[ERROR]: {message}")
        elif type=="warning":
            print(f"[WARNING]: {message}")
        elif type=="info":
            print(f"[INFO]: {message}")
        else:
            print(f"[UNKNOWN]: {message}")

res=Logger()
res.log("This is info message.", "info")   
res.log("This is a warning message.", "warning")        
res.log("This is an error message.", "error")           
