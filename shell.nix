{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

	packages = [
		(pkgs.python313.withPackages(pypkgs: with pypkgs; [
			textual
			rich
		]))
	];

	env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
		pkgs.stdenv.cc.cc.lib
		pkgs.libz
	];

}
