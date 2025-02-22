from setuptools import setup, find_packages

setup(
    # App Information
    name='Rally',  # Changed from 'Voxel Adventure'
    version='1.0.0',  # Your game version
    description='A racing game built with Ursina.',
    author='Shivam',
    url='https://github.com/mandaw2014/Rally',  # Optional

    # Android Package Information
    packages=find_packages(),
    package_data={'game': [
        '**/*.0',
        '**/*.1',
        '**/*.2',
        '**/*.bat',
        '**/*.blend',
        '**/*.csv',
        '**/*.ico',
        '**/*.idx',
        '**/*.jpg',
        '**/*.json',
        '**/*.md',
        '**/*.mp3',
        '**/*.mtl',
        '**/*.non_patched',
        '**/*.obj',
        '**/*.pack',
        '**/*.png',
        '**/*.psd',
        '**/*.py',
        '**/*.rev',
        '**/*.sample',
        '**/*.ttf',
        '**/*.txt',
        '**/*.ursinamesh',
        '**/*.wav',
        '**/*.whl'
    ]},

    # Application ID - This should be unique for your game
    android_package='com.rally.game',  # Changed from 'com.voxeladventure.game'

    # Version Code - Increment this for each Play Store update
    android_version_code=1,

    # Entry Point - This is where the game starts
    entry_points={
        'gui_scripts': [
            'Rally = game.main:main'  # Changed from 'VoxelAdventure'
        ]
    },

    # Icons and Graphics
    options={
        'android': {
            'requirements': 'ursina==4.1.1,ursinanetworking==2.1.4,panda3d,protobuf',
            'android_api': 31,  # Target Android API Level
            'ndk_version': '21.4.7075529',  # NDK Version
            'package': 'com.rally.game',  # Changed from 'com.voxeladventure.game'
            'name': 'Rally',  # Changed from 'Voxel Adventure'
            'orientation': 'landscape',
            'presplash': 'ursina/textures/ursina_logo.png',  # Using Ursina's default splash screen
            'icon': 'ursina/textures/ursina.ico',  # Using Ursina's default icon
            'presplash_color': '#000000',  # Optional splash background color
        }
    },

    # Ursina Assets - Don't remove this line
    include_package_data=True,
    package_data={'': ['ursina_assets/**']},

    # Required Files and Folders
    data_files=[
        ('ursina_assets', ['ursina_assets/**']),
        ('game', ['game/**']),
    ],

    # Dependencies - Updated for Rally
    install_requires=[
        'ursina==4.1.1',  # Changed to required version
        'ursinanetworking==2.1.4',  # Added networking dependency
        'panda3d',
        'protobuf==3.20.0'
    ],
)
