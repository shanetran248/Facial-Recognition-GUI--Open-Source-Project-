Installation

Requirements: 
- Python 3.6 (or later) 
- MacOS 

Step 1: Install Python 3.6+ 

Ensure that Python 3.6 or later is installed on your system. 
To verify that Python is installed, open a terminal(or command prompt) and run: 

    python --verion 
  

Step 2: Install Homebrew
For macOS users, Homebrew is a package manager that simplifies the installation of software. 

1. Open a terminal and run:
   
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. After installation, verify Homebrew is installed:

        brew --version   
Step 3: Install CMake 

CMake is required for compiling the dlib library, which is a core dependancy. Dlib relies on C++ code, so CMake helps in configuring and building this code to work on your system. 

Install CMake using Homebrew: 

    brew install cmake 

Step 4: Install Xcode Command Line Tools 

The Xcode Command Line Tools provide the necessary C++ compliers.

    xcode-select --install

Step 5: Install dlib 

Dlib is the core library that powers face_recognition. 

Step 5.1: Clone the dlib Repository 
  1. Download the source code for dlib

          git clone https://github.com/davisking/dlib.git cd dlib 
Step 5.2: Build the Main dlib library
  1. Create a build directory:

         mkdir build
         cd build
  2. Configure the build with CMake:

         cmake ..

  3. Complie the dlib library:

         cmake --build . 

Step 5.3: Install the Python Bindings for dlib 
  1. Navigate back to the dlib directory:

         cd ..
  2. Install the Python bindings:

         python3 setup.py install
     
  3. Test the installation: 

         python3 -c "import dlib"

     If no errors appear, dlib is installed successfully. 


Step 6: Install face_recognition 

Once dlib is installed, install the face_recognition library. 

  1. Use pip to install:

    pip install face_recognition

  2. Verify the installation:
     
    python3 -m face_recognition --help


Troubleshooting 

1. Compilation Errors:

- Ensure CMake and the required compilers are installed.
- Make sure Xcode Command Line Tools are installed.

2. Import Errors:

- Check that dlib and face_recognition were installed in the same Python environment you're using.
- Run python3 -m pip list to confirm that dlib and face_recognition are listed.








