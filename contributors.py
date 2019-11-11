import pandas as pd

def who_is_a_contributor():
	with open('README.md', 'rt') as fl:
	    lines = fl.read()
	    lines = lines[lines.find('## Contributors'):lines.find('## References and learning resources')]
	    print(lines)


if __name__ == '__main__':
	print('Who is a contributor:')
	who_is_a_contributor()
