with import <nixpkgs> {};
with pkgs.python35Packages;

buildPythonPackage rec {
  name = "alicemusic-${version}";
  version = "0.1.0";
  propagatedBuildInputs = [ pafy flask click youtube-dl sh pkgs.ffmpeg];

  src = ./.;

  buildInputs = [ pkgs.glibcLocales ];
  LC_ALL="en_US.UTF-8";

}
