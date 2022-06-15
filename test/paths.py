import os



data_path = os.path.join('..', 'data')
input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)

output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

input_path_shp = os.path.join(input_path, 'shp')
os.makedirs(input_path_shp, exist_ok=True)

output_path_kml = os.path.join(output_path, 'kml')
os.makedirs(output_path_kml, exist_ok=True)

output_path_gpkg = os.path.join(output_path, 'gpkg')
os.makedirs(output_path_gpkg, exist_ok=True)

output_path_gjson = os.path.join(output_path, 'gjson')
os.makedirs(output_path_gjson, exist_ok=True)

output_path_maps = os.path.join(output_path, 'maps')
os.makedirs(output_path_maps, exist_ok=True)

output_path_tabs = os.path.join(output_path, 'tabs')
os.makedirs(output_path_tabs, exist_ok=True)