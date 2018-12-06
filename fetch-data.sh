#!/bin/bash

cd processed_data/
wget www-personal.umich.edu/~naitian/processed_data_small.tar.gz
tar -xzvf processed_data_small.tar.gz
rm processed_data_small.tar.gz
chmod +r *.csv
cd ..
