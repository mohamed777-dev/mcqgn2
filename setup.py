from setuptools import find_packages , setup 
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='sunny',
    author_email='sunny.savita@ineuron.ai',
    install_requires=['langchain','openai',
                      'python-dotenv','streamlit','PyPDF2'],
    packages=find_packages()
)