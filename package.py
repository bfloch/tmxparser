name = "tmxparser"

version = "2.1.0.pvx1"

authors = [
    "Tamir Atlas, Andrew Kelley et al."
]

description = \
    """
    C++ library for parsing the maps generated by the Map Editor called Tiled.
    """

build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Fedora-28"],
]

config = {
    "local_packages_path": "${PVX_REZ_LOCAL_THIRDPARTY_DIR}",
    "release_packages_path": "${PVX_REZ_RELEASE_THIRDPARTY_DIR}",
}

uuid = "repository.tmxparser"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.TMXPARSER_INCLUDE_DIR = "{root}/include"
    env.TMXPARSER_LIB_DIR = "{root}/lib"
    env.TMXPARSER_LIBRARIES = "tmxparser"
