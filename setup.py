from setuptools import setup

setup(
    name='Rally',
    options={
        'build_apps': {
            # Build Rally.exe as a GUI application
            'gui_apps': {
                'Rally': 'main.py',
            },

            # Set up output logging, important for GUI apps!
            'log_filename': '$USER_APPDATA/Rally/output.log',
            'log_append': False,

            # Files to include
            'include_patterns': [
                'assets/**',
                'highscore/**',
                'tracks/**',
                'UrsinaAchievements/**',
                'models_compressed/**',

                '**/*.jpg',
                '**/*.png',
                '**/*.obj',
                '**/*.ttf',
                '**/*.wav',
                '**/*.mp3',
                '**/*.ogg',
                '**/*.bam',
            ],

            # Files to exclude
            'exclude_patterns': [
                '.git/**',
                '.github/**',
                'build/**',
                'screenshots/**',
                'mtl/**',
                '__pycache__/**',
                '**/__pycache__/**',
                'venv/**',
                'venv313/**',
                '**/*.pyc',
                '**/*.mtl',
                '**/*.md',
                'setup.py',
                'requirements.txt',
                '.gitignore',
            ],

            'include_modules': {
                '*': ['ursina']
            },

            # Include the OpenGL renderer and OpenAL audio plug-in, and ffmpeg for mp3
            'plugins': [
                'pandagl',
                'p3openal_audio',
                'p3ffmpeg',
            ],

            'platforms': [
                'manylinux2014_x86_64',
                'macosx_10_13_x86_64',
                'win_amd64',
            ],

            'prefer_discrete_gpu': True,
            'strip_docstrings': True,

            'icons': {
                # The key needs to match the key used in gui_apps/console_apps.
                # Alternatively, use "*" to set the icon for all apps.
                'Rally': ['panda3d-logo.png'],
            },
        }
    }
)
