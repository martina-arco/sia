#!/bin/bash
mkdir output
mvn package | tee output/student_package_result.txt
cd ..
mvn install:install-file -Dfile=./sia-2019-1c-04/target/gps-1.0.jar -DgroupId=ar.edu.itba.sia -DartifactId=gps -Dversion=1.0 -Dpackaging=jar | tee ./sia-2019-1c-04/output/student_package_installing_result.txt
cd itba_sia_test
mvn package | tee ../sia-2019-1c-04/output/test_result.txt
