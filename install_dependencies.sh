chmod +x install_dotnet.sh install_python.sh install_pip_libs.sh

./install_dotnet.sh
./install_python.sh
source /venv/bin/activate
./install_pip_libs.sh
