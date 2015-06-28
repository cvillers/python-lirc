from setuptools import setup, Extension

###########################################################
# Special behavior for SWIG
#
# The list of Python files to copy is created *before* build_ext runs.
# However, build_ext outputs a Python file (generated by SWIG).
# Therefore, we will define a custom build and install commands to ensure
# build_ext runs before the main build.
###########################################################
from distutils.command.build import build
from setuptools.command.install import install

class CustomBuild(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)


class CustomInstall(install):
    def run(self):
        self.run_command('build_ext')
        self.do_egg_install()

###########################################################

setup(
    cmdclass={'build': CustomBuild, 'install': CustomInstall},

    name='lirc-python',
    version='0.1',
    url='https://github.com/cvillers/lirc-python',
    license='MIT',
    author='Cameron Villers',
    author_email='cameron@ville.rs',
    description='Library for accessing and communicating with LIRC',

    packages=["lirc.client", "lirc.internal"],

    # FIXME the include path should not be hardcoded - offer a LIRC_INCLUDE variable to override
    ext_modules=[Extension("lirc.internal.lirc_client",
                           ["lirc/internal/lirc_client.i"],
                           swig_opts=["-I/usr/include/lirc"],
                           include_dirs=["/usr/include/lirc"],
                           libraries=["lirc_client"])],

    keywords="lirc infrared",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries"
    ]
)