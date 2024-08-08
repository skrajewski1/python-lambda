from awscode import listInstances, startInstances

dev_filter=[{'Name': 'tag:env', 'Values': ['dev']}]

instances = listInstances(dev_filter)
startInstances(instances)