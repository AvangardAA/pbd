```sh
sudo apt install python3.12-venv -y
python3 -m venv ~/env && source ~/env/bin/activate
pip install -r ~/pbd/requirements.txt
curl -L -o ~/duck.zip "https://github.com/duckdb/duckdb/releases/download/v1.1.3/duckdb_cli-linux-amd64.zip"
unzip ~/duck.zip
```

```sh
curl -L -o ~/pbd/hw4/pbd/seeds/archive.zip "https://www.kaggle.com/api/v1/datasets/download/valakhorasani/mobile-device-usage-and-user-behavior-dataset"
cd ~/pbd/hw4/pbd/seeds && unzip archive.zip && rm -f archive.zip
```