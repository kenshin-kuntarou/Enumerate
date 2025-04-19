## Enumerate Tool

This was a simple tool that I developed in Python for 
that a submaster enumeration can be made quickly.

It comes with some Wordlists you can use to make your
enumerations. However, if you want to use other Wordlists with the 
Tool, you can do by typing "`wordlists`" on your Kali-Linux

--- 

### Install

The command below can be used to easily install the tool.

```
git clone https://www.github.com/kenshin-kuntarou/Enumerate ~/Downloads/Enumerate
```
---

### Arguments

Here I will be listing all the arguments you can use
In the command line of your terminal to run the tool.

`-url`: Here you will pass the domain URL (required)
```
python3 enumerate.py -url 'https://exemplo.com/' 
```

`-file`: Here you will pass the Wordlist directory (required)

```
python3 enumerate.py -file 'wordlists/test.txt'
```

`-threads`: Here you will pass the number of threads you want to use

```
python3 enumerate.py -threads 20
```

---
