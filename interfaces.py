from abc import abstractmethod

class base_job_template():
    def __init__(self, job_name , parameters, job_id , vm_id):
        self.job_name = job_name
        self.parameters = parameters
        self.job_id = job_name
        self.vm_id = vm_id
        self.is_enabled=True
        self.status = None

    @abstractmethod    
    def check_enabled(self):
        """
        for each job, perform checks to see:
         if the job needs to be executed or already satisfied
        """
        return self.is_enabled

    @abstractmethod
    def parameter_evaluator(self):
        """
            Given there are parameters passed on to the job, check for place holders and evaluate the job with appropriate actual values that can be passed on to jenkins
            not all parameters needs to be passed on to jenkins            
        """
        pass
    
    @abstractmethod
    def execute(self):
        """
        this method is used to execute the job
        pass the required parameters to jenkins, 
        get back the status from jenkins
        """
        return self.status
    
    @abstractmethod
    def get_status(self):
        """
            Generic method to get the status of the run
        """
        pass

    def process(self):
        """
        generic method to do the job processing 
        """
        self.parameter_evaluator()
        if(self.check_enabled()):
            status = self.execute()
        
        return status

class run_regression(base_job_template):
    
    def check_enabled(self):
        return True
    
    def parameter_evaluator(self):
        build_number = self.job_id # get the build number from db
        build_installed_path = ""#get the build installed path from DB
        self.parameters["build_path"]= build_installed_path

    def execute(self):
        #connect to jenkins
        #trigger job with the required parameters
        #return the status
        return self.status

    def get_status(self):
        pass



parameters={
    "build_path":"$BUILD_PATH",
    "TUI_Path":"",
    "Session_File_path":"",
    "KATATF_Config_path":"",
    "POR":""
}
AMQ = run_regression("AMQ",parameters, 1,'CODEDUIW2K8VM24')
status = AMQ.execute()
