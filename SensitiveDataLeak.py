

class tactfulDataLeak():
    
    def tactfulDataCheck(self, vector, response, tactful):
        
        for item in tactful:
            if item in response.text:
                logger.info("Page: %s\n  Form: %s\n  Vector: %s\n  Status:Code: %s\n" (url, form, vector, response.status_code))
                
                
    def execute(self, pages, session, tactics):
        
        vectors = tactics._getVectors()
        
        logger.info("" + tactics.options.random)
        
        for page in pages:
            forms = page.get("inputs").get("forms")
            url = page.get("url")
        
            if tactics.options.random == "False" or tactics.options.random == "false":   
                for form in forms:
                    for vectors in vectors:
                        response = tactics._executeVector(url, vector, form)
                        
                        if response != None:
                            tactful = open(tactics.options.tactful, "r").read().splitlines()
                            self.tactfulDataCheck(vector, response, tactful)
            
            else:
                if len(forms)> 0:
                    form = random.choice(forms)
                    for vector in vectors:
                        response = tactics._executeVector(url, vector,form)
                        
                        if response != None:
                            tactful = open(tactics.options.tactful, "r").read().splitlines()
                            self.tactfulDataCheck(vector, response, tactful)
                            
        logger.info("done")
                                
                        