{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/d12178b1c4a6ef1232c8c677573ba9db204e66ff.tar.gz") {} }:

with pkgs;
(python3.withPackages (ps: with ps; [
  mypy
])).env