#!/bin/bash


install_njmon() {
     
    sudo apt install unzip
    sudo wget http://sourceforge.net/projects/nmon/files/njmon_linux_binaries_v71.zip -P ./workload_profiler/
    loc=$(sudo find / -name "workload_profiler")
    sudo unzip $loc/njmon_linux_binaries_v71.zip -d $loc/installation_files
    sudo chmod u+x $loc/installation_files/ninstall
    loc2=$(sudo find / -name "installation_files")
    cd $loc2
    sudo ./ninstall njmon_Ubuntu20_x86_64_v71
    
}

install_njmon
