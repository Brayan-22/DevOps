#Manejo de versiones de python en ubuntu
## Habilitar el repositorio PPA deadsnakes que contiene las versiones de python
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
```
##Instalar la version deseada
```bash
sudo apt install python<3.**>
```

##Instalar otra version de python
```bash
sudo apt install python3.11
sudo apt install python3.10
sudo apt install python3.9
```

##Listar las versiones de python instaladas
```bash
ls -l /usr/bin/python*
```


##Configurar el manejo de versiones de python
```bash
python3 --version
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 <1>
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 <prioridad>
sudo update-alternatives --config python3
python3 --version
```
