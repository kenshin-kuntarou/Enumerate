## Enumerate Tool

Essa foi uma ferramenta simples que eu desenvolvi em Python para 
que se possa fazer uma enumeração de sub diretórios rapidamente.

Ele vem com algumas wordlists que você pode usar para fazer as suas
enumerações. Entretanto, se você desejar usar outras wordlists com a 
ferramenta, você pode fazer digitando "`wordlists`"  no seu kali-linux

--- 

### Instalação

O comando abaixo poderá ser usado para instalar facilmente a ferramenta.
Se deseja você pode alterar o caminho da instalação como desejar

```
git clone https://www.github.com/kenshin-kuntarou/Enumerate ~/Downloads/
```
---

### Argumentos

Aqui eu estarei listando todos os argumentos que você poderá usar
na linha de comando do seu terminal para executar a ferramenta.

`-url`: Aqui você irá passar a url do domínio (obrigatório)

```
python3 enumerate.py -url 'https://exemplo.com/' 
```

`-file`: Aqui vpcê irá passar o diretório da wordlist (obrigatório)

```
python3 enumerate.py -file 'wordlists/test.txt'
```

`-threads`: Aqui você irá passar o número de threads que deseja usar

```
python3 enumerate.py -threads 20
```

---
