from distutils.core import setup

setup(name="libmich",
      author="Benoit Michau",
      author_email="michau.benoit@gmail.com",
      url="http://michau.benoit.free.fr/",
      description="A library to manipulate various data formats and network protocols",
      long_description=open("README.txt", "r").read(),
      version="0.2.3",
      license="GPLv2",
      packages=["libmich", "libmich.core", "libmich.formats", "libmich.utils", "libmich.asn1", "libmich.mobnet"])
