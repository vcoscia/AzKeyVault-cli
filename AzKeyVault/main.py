## Author: Vincenzo Coscia
## Purpose: Manage Azure keyvault secrets using Azure SDK Python
from .library.azOps import AzureKeyVaultOperations
from .library.utils import * 
import os
import getpass

def main():
    keyVaultName = input("Please provide Azure keyvault name:")
    azureops = AzureKeyVaultOperations(keyVaultName)
    azureops.loginToKeyVault(keyVaultName)
    while True:
        os.system("clear")
        log(welcome("Azure KeyVault"))
        log(f"Using keyvault: {keyVaultName}")
        log("\nChoose an action to perform    : ")
        log("""
        1 : List Secrets 
        2 : Show a secret value
        3 : Create/Update a secret
        4 : Delete a secret 
        Press any other key to Exit... 
        """)
        choice = input("\nEnter your choice : ")

        if choice == '1':
            secrets = azureops.retriveSecretsList()
            if len(secrets) > 0 :
                printAsTable({'secrets':secrets})
            else: 
                error("No Secrets found...")
        elif choice == '2' :
            selectSecret = input("Please provide secret name as saved on Azure: ")
            azureops.retriveSecret(selectSecret)
        elif choice == '3' :
            secret_name = input('Provide secret name: ')
            secret_value = getpass.getpass('Provide secret value: ')
            azureops.createSecret(secret_name,secret_value)

        elif choice == '4' :
            selectSecret = input("Please provide secret name as saved on Azure: ")
            azureops.deleteSecret(selectSecret)
        else: 
            log("Bye Bye")
            exit()
        input("Press a key to continue... ")
        os.system("clear")
        


if __name__ == "__main__":
    main()