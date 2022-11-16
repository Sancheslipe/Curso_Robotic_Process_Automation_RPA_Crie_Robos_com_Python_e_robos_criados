import requests

url = "https://www.sintegraws.com.br/api/v1/execute-api.php"

querystring = {"token":"Iy1JPISuS4azpg-i5nM1vpYv0_IjZYPeLQZY1MKB",
                    "cnpj":"85.098.929/0001-58",
                    "timeout":300}

response = requests.request("GET", url, params=querystring)

print(response.text)

https://api.infosimples.com/api/v2/consultas/sintegra/unificada?token=FMLBQuzoRoJf6FETx9y3PEOhSr2H6PFI4FsJwiP7&timeout=300&uf=SC&cnpj=85.098.929%2F0001-58&ie=&ie_produtor=&cpf=