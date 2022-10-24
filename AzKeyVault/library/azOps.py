from azure.identity import InteractiveBrowserCredential,DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError,AzureError,HttpResponseError
from .utils import * 


class AzureKeyVaultOperations():

    def __init__(self, keyVaultName ):
        self.keyVaultName = keyVaultName
        self.KVUri = f"https://{keyVaultName}.vault.azure.net/"

    def __del__(self):
        yield
        #self.credential.close()

    def loginToKeyVault(self,keyVaultName):
        '''
        Authenticate user using InteractiveBrowserCredentials
        '''
        self.credential = InteractiveBrowserCredential(additionally_allowed_tenants=['*'])
        self.credential.authenticate()
        self.client =    SecretClient(vault_url=self.KVUri, credential=self.credential)



    def retriveSecretsList(self):
        '''
        Retrive Secrets 
        '''
        secrets =  self.client.list_properties_of_secrets()
        temp = [] 
        for s in secrets: 
            temp.append(s.name)
        return temp

    def retriveSecret(self,secretName):
        try: 
            secret = self.client.get_secret(secretName)
            self.printSecret(secret)
        except ResourceNotFoundError: 
            error("No secret found with this name")
        except HttpResponseError : 
            error("Bad char in secret name")


    def printSecret(self,secretObject):
        print(f"{secretObject.name} : {secretObject.value}")

    def createSecret(self,secretName,secretValue):
        try:
            self.client.set_secret(secretName,secretValue)
            log("New secret has been saved")
        except HttpResponseError : 
            error("Bad char in secret name")

    def deleteSecret(self,secretName):
        log(f"I'm going to delete {secretName}. Please wait...")
        try: 
            deleted_secret = self.client.begin_delete_secret(secretName).result()
        except ResourceNotFoundError: 
            error("No secret found with this name")
        except HttpResponseError : 
            error("""
            HTTP error. The causes could be:
            - Bad char in secret name
            - The secret is in Azure bin and it is waiting to be purged.  
            """)
        else: 
            log("Print summary:")
            log(f"Secret name: {deleted_secret.name}")
            log(f"Secret deleted date: {deleted_secret.deleted_date}")

    if __name__ == '__main__':
        print("This class must be used inside another python script. Exit...")
        exit(1)