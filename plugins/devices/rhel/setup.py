from setuptools import setup, find_packages

setup(
    name='opsmgr-plugins-devices-rhel',
    version='0.1',

    description='Operational Manager Device Plugin for RedHat Enterprise Linux',

    author='',
    author_email='',

    url='',

    classifiers=[
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 ],

    platforms=['Any'],

    scripts=[],

    namespace_packages=['opsmgr','opsmgr.plugins','opsmgr.plugins.devices'],

    provides=['opsmgr.plugins.devices.rhel'],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'opsmgr.inventory.interfaces.IManagerDevicePlugin': [
            'Rhel = opsmgr.plugins.devices.rhel.RhelManagerPlugin:RhelPlugin',
        ],
    },

    zip_safe=False,
)
