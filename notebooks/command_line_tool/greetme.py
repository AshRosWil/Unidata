import argparse

# Create an instance
parser = argparse.ArgumentParser(description='A simple program that prints a greeting to the name specified')

# Add a name argument
parser.add_argument('--name', type=str, required=True, help='Name of the person being greeted')

parser.add_argument('--greeting', type=str, default='Hello,', help='Greeting to be used')

# Parse the arguments
args = parser.parse_args()

# Print the greeting
print('{} {}'.format(args.greeting, args.name))
