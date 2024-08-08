from awscode import listInstances, stopInstances

dev_filter=[{'Name': 'tag:env', 'Values': ['dev']}]


stopInstances(listInstances(dev_filter))
