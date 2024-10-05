# VERIFICAÇÕES DE COTAS DE PARTNERSHIP

O projeto realiza análises em uma base .csv, que está armazenada na pasta
'data_raw', no qual contém informações de partners, como a quantidade de cotas
de cada um.

# FUNCIONALIDADES

O projeto tem um pipeline denominado 'code.py' que se encontra dentro da pasta
'script'. Ele realiza consultas e manipulações de dados no arquivo .csv de origem
assim criando um novo arquivo .csv que está armazenado na pasta 'data_processed'
que tem colunas de nomes dos partners e a quantidade de cotas de cada um.

# INSTALAÇÕES

Para rodar o projeto, caso esteja utilizando o Sistema operacional windows,
é necessário instalar WLS(windows subsystem for linux) e outras dependências
anexadas no documento 'requirements.txt'
