#!/bin/bash
sudo apt-get update
sudo apt-get install -y wget
wget https://github.com/Kitware/CMake/releases/download/v3.22.2/cmake-3.22.2-linux-x86_64.tar.gz
tar -zxvf cmake-3.22.2-linux-x86_64.tar.gz
sudo cp -r cmake-3.22.2-linux-x86_64/* /usr/local/
cmake --version
