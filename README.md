Introdução
==========
O Migrant é um aplicativo auxiliar ao [MOITA](ranisalt/moita) para converter os
bancos de dados em arquivos do CAPIM para o banco de dados em documentos do
MOITA. O Migrant foi aplicado com sucesso em 30/01/2015 nos arquivos do 
MatrUFSC, convertendo com sucesso quase 7 mil arquivos.

Como usar?
==========
Só faz sentido utilizar o Migrant em um sistema que já tenha uma instalação
funcional do MOITA. Basta chamar o script e passar o arquivo de configuração do
MOITA pela flag `-m` e os arquivos à serem convertidos em seguida. O Migrant faz
a distinção entre arquivos comprimidos com gzip ou em JSON automaticamente.

```shell
./migrant.py -m /path/to/moita/config.py /path/to/capim/dados3/*.gz
```

Para maiores detalhes acesse a ajuda com a flag `-h`.