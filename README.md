# Fornecedores
## Descrição
Exercício proposto com aplicação Python e HTML.

O objetivo é abrir um arquivo CSV cuja entrada é parecida com a tabela abaixo

empresa,fornecedor,data,valor <br>
A,F1,2018-12-10,1000.00 <br>
A,F2,2018-12-11,1500.00 <br>
A,F2,2019-01-20,1500.00 <br>
A,F1,2019-01-20,2000.00 <br>
B,F2,2019-01-31,400.00  <br>
A,F3,2019-03-01,500.00  <br>
B,F3,2019-03-06,900.01  <br>
B,F1,2019-03-06,1400.00 <br>

E fornecer uma tabela em um arquivo HTML como a do print abaixo 
![alt text](https://github.com/lcslima45/fornecedores/blob/master/Screenshot%20from%202020-02-03%2021-32-27.jpg)

Onde cada linha da tabela representa o valor máximo pago a um fornecedor durante um mês
## Execução

Baixe os três arquivos deste repositório: fornecedores3.py, construtor_html.py, pagamentos_sample.csv.

No Terminal do Linux, mova com o comando cd até a pasta onde estão os três arquivos que você baixou e então 
execute o comando abaixo
```
python3 construtor_html.py
```

E o construtor construirá um arquivo html cujo nome é tabela_fornecedores.html. 

Se desejar testar o codigo-fonte com qualquer outro arquivo exibido na mesma forma de entrada do arquivo CSV fornecido aqui, basta entrar no codigo fornecedores.py e mudar o endereço do arquivo com o nome da locação do seu novo arquivo, assim como está na área circulada do print abaixo.

![alt text](https://github.com/lcslima45/fornecedores/blob/master/Screenshot%20from%202020-02-03%2022-15-53.png)

## Lógica de execução

No script referente ao arquivo fornecedores3.py

As linhas do CSV foram lidas e tratadas para uma estrutura de dados do tipo dicionário, onde são associdos um valor a uma chave. 

As chaves do dicionario é gerada na hora da leitura do arquivo e associa um mês com uma string da seguinte forma 

Ano-Mes <br>
2019-07 <br>
2019-10 <br>

Em cada chave do dicionário são salvos em uma lista as linhas do arquivo CSV que pertencem aquele mês, cada linha é um array com quatro posições, respectivamente: empresa, fornecedor, data, pagamento.

Uma vez que todos as linhas estão associdas com as suas respectivas chaves, podemos procurar o valor máximo de pagamento em cada mês.

No script referente ao arquivo construtor_html.py, os itens do dicionário são inscritos em uma tabela gerada dinâmicamente pelo arquivo fornecedores3.py. 


