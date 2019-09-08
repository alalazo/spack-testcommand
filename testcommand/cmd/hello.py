# Test an absolute import
from spack.extensions.testcommand.implementation.hello_world import hello_world

# Test a relative import
from ..implementation.hello_folks import hello_folks
from ..implementation.hello import hello_hello

description = "hello world extension command"
section = "test command"
level = "long"

# Test setting a global variable in setup_parser and retrieving
# it in the command
global_message = 'foo'

def setup_parser(subparser):
    sp = subparser.add_subparsers(metavar='SUBCOMMAND', dest='subcommand')
    global global_message
    sp.add_parser('world', help='Print Hello world!')
    sp.add_parser('folks', help='Print Hello folks!')
    sp.add_parser('global', help='Print Hello bar!')
    sp.add_parser('hello', help='Print Hello from a subcommand with the same name as the primary command!')
    global_message = 'bar'

def hello(parser, args):
    if args.subcommand == 'world':
        hello_world()
    elif args.subcommand == 'folks':
        hello_folks()
    elif args.subcommand == 'global':        
        print(global_message)
    elif args.subcommand == 'hello':
        hello_hello()
