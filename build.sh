#! /bin/bash

mkdir -p hello_packaging/usr/local/hello-world-haru
cp -r demo_app/* hello_packaging/usr/local/hello-world-haru

dpkg-deb --build hello_packaging

rm -rf hello_packaging/usr/local/hello-world-haru/*