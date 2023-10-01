sudo apt update
sudo apt upgrade
sudo apt isntall python3-pip
pip3 install jupyter
python3 -m notebook --generate-update_config

nano ~/.jupyter/jupyter_notebook_config.py

#add
c.NotebookApp.ip = '0.0.0.0'

python3 -m notebook password

#Enter password

python3 -m notebook --no-browser