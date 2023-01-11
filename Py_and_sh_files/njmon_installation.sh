#!/bin/bash

install_njmon() {
    sudo apt install unzip
    sudo wget http://sourceforge.net/projects/nmon/files/njmon_linux_binaries_v71.zip -P workload_profiler/
    sudo unzip workload_profiler/njmon_linux_binaries_v71.zip -d workload_profiler/installation_files
    sudo chmod u+x workload_profiler/installation_files/ninstall
    cd workload_profiler/installation_files
    sudo ./ninstall njmon_Ubuntu20_x86_64_v71
    
}

install_njmon
