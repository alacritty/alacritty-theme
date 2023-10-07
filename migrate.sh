#!/usr/bin/env sh
workdir=`pwd`
yamldir="${workdir}/themes"
cd "${yamldir}"
for filename in *; do
    alacritty migrate -c $filename 
done
mv ${yamldir}/*.toml ../themes-toml
