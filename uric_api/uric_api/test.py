import importlib


path,name='host.routing.application'.rsplit(".", 1)
print(path,name)
module = importlib.import_module(path)