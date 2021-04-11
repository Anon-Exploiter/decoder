from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read().strip()

setup(name='decoder',
	version='0.3',
	description='A simple script to try and decode a string in various encoding mechanisms regardless of it\'s (original) type.',
	long_description=long_description,
	long_description_content_type='text/markdown',  # This is important!
	url='https://github.com/Anon-Exploiter/decoder',
	author='Syed Umar Arfeen',
	author_email='umar.arfeen@outlook.com',
	license='MIT',
	packages=find_packages(),
	install_requires=[
		'pycipher',
		'termcolor',
	],
	entry_points={
		'console_scripts': [
			'decoder = decoder.decoder:main'
		],
	},
	zip_safe=False
)
