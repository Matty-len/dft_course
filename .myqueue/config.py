# Generated with mq config.
#
# Please review the list of node types and remove those
# that you don't want to use.  Read more about config.py
# files here:
#
#   https://myqueue.readthedocs.io/en/latest/configuration.html

config = {
    'scheduler': 'lsf',
    'nodes': [
        ('XeonE5_2650v4', {'cores': 24, 'memory': '252GB'}),
        ('XeonE5_2660v3', {'cores': 20, 'memory': '126GB'})]}