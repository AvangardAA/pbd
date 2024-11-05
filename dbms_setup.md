```sh
sudo apt install mysql-server -y
sudo apt install python3.12-venv -y
python3 -m venv ~/env
source ~/env/bin/activate && pip install -r ~/pbd/requirements.txt
```

```
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'dummy';
exit;
```