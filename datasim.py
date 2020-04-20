"""
    Run the simulation af a dataset
    Note that it's Python 2.7 friendly
"""
from __future__ import print_function
import os

# My modules
import simulation as mysim
import customconfig
reload(mysim)
reload(customconfig)


if __name__ == "__main__":
    system_config = customconfig.Properties('./system.json')  # Make sure it's in \Autodesk\MayaNNNN\
    path = system_config['templates_path']

    # ------ Dataset Example ------
    # dataset = 'test_skirt_maya_coords_200417-10-18-resumes'
    # dataset_file = os.path.join(system_config['output'], dataset, 'dataset_properties.json')
    # props = customconfig.Properties(dataset_file)
    # props.set_basic(body='f_smpl_templatex300.obj')

    # mysim.batch_sim(path, path, system_config['output'], props, caching=False)
    # props.serialize(dataset_file)

    # ------ Example for single template generation ------
    path_example = 'F:/GK-Pattern-Data-Gen/zero_grav_skirt_maya_coords_200420-14-15'
    props = customconfig.Properties(path_example + '/dataset_properties.json', True)  
    props.set_basic(
        body='f_smpl_templatex300.obj',
        templates='skirt_maya_coords_AJN7LX7IVE_specification.json'
    )
    # TODO Give path to template directly
    mysim.single_file_sim(path_example, path, props, caching=True)
    print(props)
