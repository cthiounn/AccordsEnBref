sudo apt-get install -y apt-transport-https
sudo echo "deb https://notesalexp.org/tesseract-ocr5/jammy/ jammy main" >> /etc/apt/sources.list
sudo apt-get update -oAcquire::AllowInsecureRepositories=true
sudo apt-get install -y notesalexp-keyring -oAcquire::AllowInsecureRepositories=true
sudo apt-get update
sudo apt install -y tesseract-ocr-all
sudo apt install -y poppler-utils