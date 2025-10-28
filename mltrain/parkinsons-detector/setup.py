from setuptools import setup, find_packages

setup(
    name='parkinsons-detector',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A machine learning project to detect Parkinson\'s disease from data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/parkinsons-detector',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'matplotlib',  # Optional: for visualization
        'seaborn'      # Optional: for enhanced visualization
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)