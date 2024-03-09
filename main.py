files = ['25data', '30data', '35data', '25admin', '30admin', '35admin']
for file in files:
    infile = 'd:\\IPMS\\' + file + '.txt'
    outfile = 'd:\\IPMS\\Ready\\' + file + '_clear.txt'
    list_of_acls = []
    with open(infile, 'r') as f:
        for i in f:
            if i.startswith(' '):
                list_of_acls.append(i.strip().split())

    def delete_things(my_list):
        for x in my_list:
            x.pop(0)
            x.pop(1)
            x.pop(1)
            x.pop(1)
            if len(x) >= 14:
                del x[-6:]
            if 'icmp' in x:
                del x[-4:]
        return my_list

    with open(outfile, 'w') as out:
        for x in delete_things(list_of_acls):
            while 'host' in x:
                net_value = x.index('host')
                x[net_value + 1] = x[net_value + 1] + '/32'
                x.pop(net_value)
            while '255.255.192.0' in x:
                net_value = x.index('255.255.192.0')
                x[net_value - 1] = x[net_value - 1] + '/18'
                x.pop(net_value)
            while '255.255.224.0' in x:
                net_value = x.index('255.255.224.0')
                x[net_value - 1] = x[net_value - 1] + '/19'
                x.pop(net_value)
            while '255.255.240.0' in x:
                net_value = x.index('255.255.240.0')
                x[net_value - 1] = x[net_value - 1] + '/20'
                x.pop(net_value)
            while '255.255.248.0' in x:
                net_value = x.index('255.255.248.0')
                x[net_value - 1] = x[net_value - 1] + '/21'
                x.pop(net_value)
            while '255.255.252.0' in x:
                net_value = x.index('255.255.252.0')
                x[net_value - 1] = x[net_value - 1] + '/22'
                x.pop(net_value)
            while '255.255.254.0' in x:
                net_value = x.index('255.255.254.0')
                x[net_value - 1] = x[net_value - 1] + '/23'
                x.pop(net_value)
            while '255.255.255.0' in x:
                net_value = x.index('255.255.255.0')
                x[net_value - 1] = x[net_value - 1] + '/24'
                x.pop(net_value)
            while '255.255.255.128' in x:
                net_value = x.index('255.255.255.128')
                x[net_value - 1] = x[net_value - 1] + '/25'
                x.pop(net_value)
            while '255.255.255.192' in x:
                net_value = x.index('255.255.255.192')
                x[net_value - 1] = x[net_value - 1] + '/26'
                x.pop(net_value)
            while '255.255.255.224' in x:
                net_value = x.index('255.255.255.224')
                x[net_value - 1] = x[net_value - 1] + '/27'
                x.pop(net_value)
            while '255.255.255.240' in x:
                net_value = x.index('255.255.255.240')
                x[net_value - 1] = x[net_value - 1] + '/28'
                x.pop(net_value)
            while '255.255.255.248' in x:
                net_value = x.index('255.255.255.248')
                x[net_value - 1] = x[net_value - 1] + '/29'
                x.pop(net_value)
            while '255.255.255.252' in x:
                net_value = x.index('255.255.255.252')
                x[net_value - 1] = x[net_value - 1] + '/30'
                x.pop(net_value)
            while '255.255.255.254' in x:
                net_value = x.index('255.255.255.254')
                x[net_value - 1] = x[net_value - 1] + '/31'
                x.pop(net_value)

            out.write(str(x) + '\n')